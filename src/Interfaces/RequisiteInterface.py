from src.Models.Models import Requisite
from src.Types.OrderType import RequisiteRequestType


class RequisiteInterface:


    requisite_request:RequisiteRequestType
    requisite_db_obj:Requisite
    price:float = None

    def prepare() -> tuple[str, dict]:
        ...

