from pydantic import BaseModel


class RequisiteRequestType(BaseModel):

    label:str

    food:int

    ingredients:list[int] = None

    toppings:list[int] = None



class OrderRequestType(BaseModel):

    client_name:str
    requisites:list[RequisiteRequestType]



class OrderSolicitedType(BaseModel):

    order_id:str
    price:float



class PaymentType(BaseModel):

    order_id:str
    idempotency_key:str
    amount:float



class ItemsResponseType(BaseModel):

    food:dict
    ingredients:list[dict]
    toppings: list[dict]



class RequisiteResponseType(BaseModel):

    label:str
    items: ItemsResponseType

    price:float



class OrderResponseType(BaseModel):

    order_id:str
    amount:str
    paid:str
    leftover:str

    requisites:list[RequisiteResponseType]