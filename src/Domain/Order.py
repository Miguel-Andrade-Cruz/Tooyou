from db.setup_db import db

from src.Models.Models import Order as OrderDB, Requisite as RequisiteDB
from sqlalchemy.orm import joinedload

from src.Enums.OrderStatus import OrderStatus
from src.Types.OrderType import OrderSolicitedType, OrderResponseType, RequisiteResponseType, ItemsResponseType
from src.Interfaces.RequisiteInterface import RequisiteInterface
from src.Models.Models import (
    Order as OrderDB,
    Requisite as RequisiteDB
)


class Order():

    price:float = None

    def __init__(self, id= None, requisites:list[RequisiteInterface] = None, order_id:str = None) -> None:

        if id == None:
            self.requisites:list[RequisiteInterface] = requisites
            self.order_id:str = order_id
            return

        else:
            self.order_db:OrderDB = db.session.query(Order)\
                .options(
                    joinedload(OrderDB.requisites)
                    .joinedload(RequisiteDB.ingredients),
                    joinedload(OrderDB.requisites)
                    .joinedload(RequisiteDB.toppings),
                    joinedload(OrderDB.payment)
                )\
                .filter(Order.order_id == order_id)\
                .first()
            return    





    def prepare(self) -> tuple[str ,OrderSolicitedType | list[str]]: # mudar mais tarde para um tipo: Unavailable

        response:OrderSolicitedType
        total_price:float = 0.0

        for requisite in self.requisites:
            (status, result) = requisite.prepare()
            if status == 'NOT FOUND':
                return ('NOT FOUND', {})

            total_price += requisite.price

        self.price = total_price
        response = OrderSolicitedType(
            order_id=self.order_id,
            price=total_price,
        )

        return ('OK', response)
    



    def save(self) -> None:

        requisites_db:list[RequisiteDB] = [rq.db_obj for rq in self.requisites]
        order_db:OrderDB = OrderDB(
            id=self.order_id,
            status=OrderStatus.prepared,
            price=self.price,
            requisites=requisites_db
        )
        requisites_to_save = [ req.requisite_db_obj for req in self.requisites]

        db.session.add_all(requisites_to_save)
        db.session.add(order_db)
        db.session.commit()
        
        return
    



    def as_response(self) -> OrderResponseType:

        requisites_response:list[RequisiteResponseType]

        for requisite in self.order_db.requisites:
            food_response = {
                'food': requisite.food.name,
                'price': requisite.food.price
            }

            ingredients_response:list= [ {'name': ing.name, 'price': ing.price} for ing in requisite.ingredients]
            toppings_response:list = [{'name': tpp.name, 'price': tpp.price} for tpp in requisite.toppings]

            requisites_response.append(
                RequisiteResponseType(
                    label=requisite.label,
                    price=requisite.price,
                    items=ItemsResponseType(
                        food=food_response,
                        ingredients=ingredients_response,
                        toppings=toppings_response
                    )
                )
            )

        response:OrderResponseType = OrderResponseType(
            order_id=self.order_id,
            amount=f"{self.price:.2f}",
            paid=f"{self.order_db.payment.paid:.2f}",
            leftover=f"{self.order_db.payment.leftover:.2f}",
            requisites=requisites_response            
        )

        return response
