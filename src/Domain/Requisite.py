from src.Types.OrderType import RequisiteRequestType
from src.Interfaces.RequisiteInterface import RequisiteInterface
from src.Models.Models import Requisite as RequisiteDB
from db.setup_db import db
from src.Models.Models import Food

class Requisite(RequisiteInterface):

    def __init__(self, food_request:int, label:str):
        self.requisite_label:str = label
        self.food_request:int = food_request


    def prepare(self) -> tuple[str, dict]:
        
        food:Food = db.session.query(Food).filter(Food.id == self.food_request).first()
        if not food:
            return ('NOT FOUND', {})


        self.requisite_db_obj = RequisiteDB(
            label=self.requisite_label,
            price=food.price
        )

        self.price = food.price
        requisite = {
            'label': self.requisite_label,
            'food': food.name,
            'price': food.price
        }

        return ('OK', requisite)



