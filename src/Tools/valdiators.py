from db.setup_db import db, joinedload
from src.Models.Models import Payment, Order, Requisite
from src.Types.OrderType import PaymentType, OrderResponseType, RequisiteResponseType
from src.Enums.OrderStatus import OrderStatus





def check_has_paid(order:Order, idempotency_key:str) -> bool:

    order_idempotency_key = order.payment.idempotency_key
    if order_idempotency_key == None:
        return False
    return idempotency_key == order_idempotency_key




def mmount_response_order(order:Order, amount_paid:float) -> OrderResponseType:

    result_requisites:list[RequisiteResponseType] = []
    for requisite in order.requisites:
        
        food:dict = {'name': requisite.food.name, 'price': requisite.food.price}
        ingredients:list[dict] = [{'name': ing.name, 'price': ing.price} for ing in requisite.ingredients]
        toppings:list[dict] = [{'name': tp.name, 'price': tp.price} for tp in requisite.toppings]

        result_requisite:RequisiteResponseType = RequisiteResponseType(
            label=requisite.label,
            food=food,
            ingredients=ingredients,
            toppings=toppings,
            price=requisite.price
        )
        result_requisites.append(result_requisite)

    leftover:float = amount_paid - order.price
    
    response = OrderResponseType(
        order_id=order.order_id,
        amount=order.price,
        paid=amount_paid,
        leftover=leftover,
        requisites=result_requisites
    )

    return response





def validate_order_payment(payment_request:PaymentType, order:Order) -> tuple[str, OrderResponseType | str]:

    
    if order == None:
        return ('FAIL', 'no orders found with this identifier')
    
    if payment_request.amount < order.price:
        return ('FAIL', 'amount too low')
    
    has_paid = check_has_paid(order, payment_request.idempotency_key)
        
    response:OrderResponseType = mmount_response_order(order, payment_request.amount)
    
    if has_paid:
        return ('OK', response)
    
    payment = Payment(
        order_id=order.order_id,
        amount=order.price,
        idempotency_key=payment_request.idempotency_key
    )
    order.status = OrderStatus.delivered


    db.session.add(payment)
    db.session.add(order)
    db.session.commit()
    
    return ('OK', response)
