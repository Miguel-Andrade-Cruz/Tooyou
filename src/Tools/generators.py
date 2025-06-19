from datetime import datetime
from src.Types.OrderType import PaymentType



def generate_order_id(client_name:str) -> str:

    now = datetime.now()
    now_str = now.strftime('%Y_%m_%d:%H_%M_%S')

    client_normalized = client_name.replace(' ', '_').lower()

    order_id = 'order_' + client_normalized.lower() + '_' + now_str
    return order_id
