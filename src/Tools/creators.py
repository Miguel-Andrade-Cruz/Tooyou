from src.Types.OrderType import OrderRequestType
from src.Interfaces.RequisiteInterface import RequisiteInterface
from src.Domain.Order import Order
from src.Domain.Requisite import Requisite
from src.Models.Models import Order as OrderDB
from src.Decorators.ToppingsDecorator import ToppingsDecorator
from src.Decorators.IngredientsDecorator import IngredientsDecorator

from src.Tools.generators import generate_order_id




def create_order_from_request(order_req:OrderRequestType) -> Order:

    requisites_list:list[RequisiteInterface] = []
    for requisite_request in order_req.requisites:
    
        requisite:RequisiteInterface = Requisite(food_request=requisite_request.food, label=requisite_request.label)
        if requisite_request.ingredients:
            requisite = IngredientsDecorator(requisite, items=requisite_request.ingredients)
        
        if requisite_request.toppings:
            requisite = ToppingsDecorator(requisite, items=requisite_request.toppings)

        requisites_list.append(requisite)

    order:Order = Order(requisites=requisites_list, id=generate_order_id(order_req.client_name))

    return order


def create_order_from_id(order_id:str) -> Order:

    order:Order = Order(id=order_id)

    return order