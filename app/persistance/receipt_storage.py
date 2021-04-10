#!/usr/bin/python

##################################################
## Storage controller to handle with receipts and ingredients
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

# SqlAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import config

# Modules
from app.persistance.model import model_receipt, model_ingredient
from app.persistance.model.model_ingredient import Ingredient
from app.persistance.model.model_receipt import Receipt
from app.controller.model_controller_ingredient import ModelControllerIngredient
from app.controller.model_controller_receipt import ModelControllerReceipt
from app.controller.exceptions import UnknownErrorInStorageSystem
from app.controller.exceptions import ElementNotPresent


class ReceiptStorage:

    def __init__(self):
        # create an engine
        self.engine = create_engine(
            config.Config.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
        )

        # create a configured "Session" class
        self.Session = sessionmaker(expire_on_commit=False, autocommit=False, autoflush=True, bind=self.engine)

        # Create all tables by issuing CREATE TABLE commands to the DB.
        self.create_all();

    def delete_all(self):
        model_receipt.Base.metadata.drop_all(self.engine)  # all tables are deleted
        model_ingredient.Base.metadata.drop_all(self.engine)

    def create_all(self):
        model_ingredient.Base.metadata.create_all(bind=self.engine)
        model_receipt.Base.metadata.create_all(bind=self.engine)

    def redo_db(self):
        self.delete_all()
        self.create_all()

    def set_ingredient(self, ingredient):
        session = self.Session()

        ingredient_id = -1
        try:
            insert_ingredient = Ingredient(ingredient.name, ingredient.calories);
            session.add(insert_ingredient)
            session.commit()

            ingredient_id = insert_ingredient.id
        except Exception as e:
            print(e)
            session.rollback()
            raise UnknownErrorInStorageSystem()
        finally:
            session.close()

        return ingredient_id

    def get_ingredient(self, ingredient_id):
        session = self.Session()

        ingredient = None
        try:
            read_ingredient = session.query(Ingredient) \
                .filter(Ingredient.id == ingredient_id) \
                .first()

            if read_ingredient is not None:
                ingredient = ModelControllerIngredient(read_ingredient.id,
                                                       read_ingredient.name,
                                                       read_ingredient.calories)
        except Exception as e:
            print(e)
            raise UnknownErrorInStorageSystem()
        finally:
            session.close()

        return ingredient

    def delete_ingredient(self, ingredient_id):
        session = self.Session()

        try:
            read_ingredient = session.query(Ingredient) \
                .filter(Ingredient.id == ingredient_id) \
                .first()
            if read_ingredient is not None:
                session.delete(read_ingredient)
                session.commit()
        except Exception as e:
            print(e)
            session.rollback()
            raise UnknownErrorInStorageSystem()
        finally:
            session.close()

    def update_ingredient(self, ingredient):
        session = self.Session()

        try:
            read_ingredient = session.query(Ingredient) \
                .filter(Ingredient.id == ingredient.id) \
                .first()

            if read_ingredient is not None:
                read_ingredient.name = ingredient.name
                read_ingredient.calories = ingredient.calories
                session.commit()

        except Exception as e:
            print(e)
            session.rollback()
            raise UnknownErrorInStorageSystem()
        finally:
            session.close()
            if read_ingredient is None:
                raise ElementNotPresent()

    def set_receipt(self, receipt):
        session = self.Session()
        receipt_id = -1

        try:
            ingredients = []
            # todo dnry
            for ingredient in receipt.ingredients:
                ingredients.append(Ingredient(ingredient.name,
                                              ingredient.calories))
            insert_receipt = Receipt(receipt.name, receipt.description, ingredients)

            session.add(insert_receipt)
            session.commit()

            receipt_id = insert_receipt.id
        except Exception as e:
            print(e)
            session.rollback()
            raise UnknownErrorInStorageSystem()
        finally:
            session.close()

        return receipt_id

    def get_receipt(self, receipt_id):
        session = self.Session()

        try:
            read_receipt = session.query(Receipt) \
                .filter(Receipt.id == receipt_id) \
                .first()

            if read_receipt is not None:
                ingredients = []
                for ingredient in read_receipt.ingredients:
                    ingredients.append(ModelControllerIngredient(ingredient.id,
                                                                 ingredient.name,
                                                                 ingredient.calories))

                receipt = ModelControllerReceipt(read_receipt.id,
                                                 read_receipt.name,
                                                 read_receipt.description,
                                                 ingredients)
        except Exception as e:
            print(e)
            raise UnknownErrorInStorageSystem()
        finally:
            session.close()

        return receipt

    def delete_receipt(self, receipt_id):
        session = self.Session()

        try:
            read_receipt = session.query(Receipt) \
                .filter(Receipt.id == receipt_id) \
                .first()
            if read_receipt is not None:
                session.delete(read_receipt)
                session.commit()
        except Exception as e:
            print(e)
            session.rollback()
            raise UnknownErrorInStorageSystem()
        finally:
            session.close()

    def update_receipt(self, receipt):
        session = self.Session()

        try:
            read_receipt = session.query(Receipt) \
                .filter(Receipt.id == receipt.id) \
                .first()

            if read_receipt is not None:
                read_receipt.name = receipt.name
                read_receipt.description = receipt.description
                ingredients = []
                # todo dnry
                for ingredient in receipt.ingredients:
                    ingredients.append(Ingredient(ingredient.name,
                                                  ingredient.calories))
                read_receipt.ingredients = ingredients
                session.commit()

        except Exception as e:
            print(e)
            session.rollback()
            raise UnknownErrorInStorageSystem()
        finally:
            session.close()
            if read_receipt is None:
                raise ElementNotPresent()
