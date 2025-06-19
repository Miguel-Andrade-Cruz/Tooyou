from functools import reduce

from db.setup_db import db
from .RequisiteDecorator import RequisiteDecorator
from Models.Models import Ingredient


class IngredientsDecorator(RequisiteDecorator):

    def prepare(self) -> tuple[str, dict]:
        (status, result) = self.wrapped.prepare()

        if status == 'NOT FOUND':
            return ('NOT FOUND', {})            

        ingredients:list[Ingredient] = []
        for item in self.items:

            ingredient = db.session.query(Ingredient).filter(Ingredient.id == item).first()
            if ingredient == None:
                return ('NOT FOUND', {})
            
            ingredients.append(ingredient)

        self.requisite_db_obj.ingredients = ingredients

        ingredients_mapped:list[dict] = map(lambda ing: {'ingredient': ing.name, 'price': ing.price}, ingredients)
        ingredients_total_price:float = reduce(lambda carry, ing: carry + ing.price, ingredients_mapped)

        self.wrapped.price += ingredients_total_price
        result.update({'ingredients': ingredients_mapped})
        
        return ('OK', result)

