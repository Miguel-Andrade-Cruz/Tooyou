from db.setup_db import db
from Models.Models import Food, Ingredient, Topping
from Types.DisposablesType import DisposablesType


def searchDisposableItems(category:str, item_id:int = None) -> tuple[ str, DisposablesType | str]:

    if not item_id == None:
        item:Food | Ingredient | Topping = db.session.query(category).filter(category.id == item_id).first()

        if item == None:
            return ('FAIL', 'item not found')

        disposables = DisposablesType(items=[{'name': item.name, 'price': item.price}])
        return ('OK', disposables)
    
    items:list[Food | Ingredient | Topping] = db.session.query(category).all()

    disposables = [{'id': it.id, 'name': it.name, 'price': it.price} for it in items]
    disposables = DisposablesType(items=disposables)

    return ('OK', disposables)