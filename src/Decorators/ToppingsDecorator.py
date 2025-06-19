from functools import reduce

from db.setup_db import db
from .RequisiteDecorator import RequisiteDecorator
from Models.Models import Topping


class ToppingsDecorator(RequisiteDecorator):

    def prepare(self) -> tuple[str, dict]:

        (status, result) = self.wrapped.prepare()
        if status == 'NOT FOUND':
            return ('NOT FOUND', {})
        
        toppings:list[Topping] = []
        for item in self.items:

            topping = db.session.query(Topping).filter(Topping.id == item).first()
            if topping == None:
                return ('NOT FOUND', {})
            
            toppings.append(topping)

        self.requisite_db_obj.toppings = toppings

        toppings_mapped:list[dict] = map(lambda tpp: {'topping': tpp.name, 'price': tpp.price}, toppings)
        toppings_total_price:float = reduce(lambda carry, tpp: carry + tpp.price, toppings_mapped)

        self.wrapped.price += toppings_total_price
        result.update({'toppings': toppings_mapped})
        
        return ('OK', result)


