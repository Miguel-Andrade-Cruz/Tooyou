from typing import Literal

import uvicorn
from fastapi import FastAPI, Response, status

from Types.OrderType import (
    OrderRequestType,
    PaymentType
)
from Tools.creators import create_order_from_request, create_order_from_id
from Tools.valdiators import validate_order_payment as validate_payment
from Tools.handlers import searchDisposableItems as disposableItems
from Domain.Order import Order

app = FastAPI()



@app.get('/disposable/{item_id}')
def view_foods(response:Response, category:Literal['food', 'ingredient', 'topping'], item_id:int = None):
    
    (disposable_status, result) = disposableItems(category.capitalize(), item_id)
    if disposable_status == 'FAIL':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'message': 'error',
            'description': result
        }

    response.status_code = status.HTTP_200_OK
    return {
        'message': 'ok',
        'disposable_items': result
    }




@app.post('/order')
def make_order(order_req:OrderRequestType, response:Response):
    
    order:Order = create_order_from_request(order_req)
    (order_status, result) = order.prepare()

    if order_status == 'NOT FOUND':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'message': 'error',
            'description': 'some items in order doesnt exist',
        }

    elif order_status == 'OK':

        order.save()      
        response.status_code = status.HTTP_201_CREATED
        return {
            'message': 'ok',
            'description': 'your order was created sucessfully',
            'order': result
        }




@app.post('order/pay')
def pay_order(payment_request:PaymentType, response:Response):
    
    order:Order = create_order_from_id(payment_request.order_id)
    (payment_status, result) = validate_payment(payment_request, order)

    if payment_status == 'FAIL':
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            'message': 'error',
            'description': result
        }
    
    response.status_code == status.HTTP_202_ACCEPTED
    return {
        'message': 'payment realised sucessfully',
        'order': order.as_response()
    }








if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)