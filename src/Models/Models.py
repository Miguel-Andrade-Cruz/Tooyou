from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from src.Enums.OrderStatus import OrderStatus

class Base(DeclarativeBase):
    pass



class Payment(Base):

    __tablename__ = 'payments'
    
    id: Mapped[int] = mapped_column(primary_key=True)

    order: Mapped['Order'] = relationship(viewonly=True)
    amount: Mapped[float] = mapped_column()
    paid: Mapped[float] = mapped_column()
    leftover: Mapped[float] = mapped_column()
    idempotency_key: Mapped[str] = mapped_column(unique=True)



class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[str] = mapped_column(primary_key=True)
    
    payment_id: Mapped[int] = mapped_column(ForeignKey('payments.id'))
    payment: Mapped['Payment'] = relationship()
    status: Mapped[OrderStatus] = mapped_column(default=OrderStatus.prepared)
    price: Mapped[float] = mapped_column()

    requisites: Mapped[list['Requisite']] = relationship()



class Requisite(Base):
    __tablename__ = 'requisites'

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    food_id: Mapped[int] = mapped_column(ForeignKey('foods.id'))

    label: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    food: Mapped['Food'] = relationship()
    ingredients: Mapped[list['Ingredient']] = relationship(secondary='assoc_ingredients')
    toppings: Mapped[list['Topping']] = relationship(secondary='assoc_toppings')





class AssociateIngredient(Base):
    __tablename__ = 'assoc_ingredients'

    requisite_id: Mapped[int] = mapped_column(ForeignKey('requisites.id'), primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey('ingredients.id'), primary_key=True)


class AssociateTopping(Base):
    __tablename__ = 'assoc_toppings'

    requisite_id: Mapped[int] = mapped_column(ForeignKey('requisites.id'), primary_key=True)
    topping_id: Mapped[int] = mapped_column(ForeignKey('toppings.id'), primary_key=True)





class Food(Base):
    __tablename__ = 'foods'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()



class Topping(Base):
    __tablename__ = 'toppings'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()



class Ingredient(Base):
    __tablename__ = 'ingredients'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()