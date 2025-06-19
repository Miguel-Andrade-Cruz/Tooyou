from src.Types.OrderType import OrderRequestType, RequisiteRequestType
from src.Models.Models import Food, Ingredient, Topping



    
MOCK_FOOD__BEEF = OrderRequestType(
    client_name='Jose Bonifacio',
    requisites=[
        RequisiteRequestType(
            label='Meu bife',
            food=2
        )
    ]
)

MOCK_FOOD__STROGONOFF = OrderRequestType(
    client_name='Francisco Glicerio',
    requisites=[
        RequisiteRequestType(
            label='Estrogonoffe do Fran',
            food=1
        )
    ]
)

MOCK_INGREDIENTS__FOOD_STROGONOFF = OrderRequestType(
    client_name='Nébias',
    requisites=[
        RequisiteRequestType(
            label='Nofão do Nebião',
            food=2,
            ingredients=[1, 2],
        )
    ]
)

MOCK_TOPPINGS__FOOD_BEEF =  OrderRequestType(
    client_name='Siqueira Campos',
    requisites=[
        RequisiteRequestType(
            label='Bifin do senhor Campos',
            food=1,
            ingredients=[1, 2, 3],
            toppings=[2, 3]
        )
    ]
)

MOCK_MULTIPLE_REQUISITES__FOOD_STROGONOFF_BEEF = OrderRequestType(
    client_name='Washington',
    requisites=[
        RequisiteRequestType(
            label='bife para seu Luís',
            food=1,
            ingredients=[1, 2],
            toppings=[3]
        ),

        RequisiteRequestType(
            label='estrogonofe para luisa',
            food=2,
            ingredients=[2],
            toppings=[1, 2]
        )
    ]
)


MOCK_STROGONOFF = Food(id=1, name='Bfe á milanesa', price=12)
MOCK_BEEF = Food(id=2, name='Estrogonofe', price=30)
    
MOCK_CHEESE = Ingredient(id=1, name='Queijo Parmesão', price=2)
MOCK_SAUCE = Ingredient(id=2, name='Molho Pesto', price=5)
MOCK_MILK = Ingredient(id=3, name='Leite', price=9)


MOCK_GARLIC = Topping(id=1, name='Alho frito', price=1)
MOCK_SALT= Topping(id=2, name='Sal', price=3)
MOCK_PEPPER = Topping(id=3, name='Pimenta biquinho', price=12)