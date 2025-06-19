import pytest
from freezegun import freeze_time
from .mocks.RequestMocks import *


@pytest.mark.parametrize('input_request, mock_database, expected', [
    (
        MOCK_FOOD__BEEF,
        MOCK_BEEF,
        {
           'order_id': 'order_jose_bonifacio_2025_06_18:22_36_57',
           'price': 12
        }
    ),
    (
        MOCK_FOOD__STROGONOFF,
        MOCK_STROGONOFF,
        {
            'order_id': 'order_francisco_glicerio_2025_06_18:22_36_57',
            'price': 30
        }
    ),
    (
        MOCK_INGREDIENTS__FOOD_STROGONOFF,
        {
            'FOOD': MOCK_STROGONOFF,
            'INGREDIENTS': [MOCK_CHEESE, MOCK_SAUCE]
        },
        {
            'order_id': 'order_nébias_2025_06_18:22_36_57',
            'price': 37
        }
    ),
    (
        MOCK_TOPPINGS__FOOD_BEEF,
        {
            'FOOD': MOCK_BEEF,
            'INGREDIENTS': [MOCK_CHEESE, MOCK_SAUCE, MOCK_MILK],
            'TOPPINGS': [MOCK_SALT, MOCK_PEPPER]
        },
        {
            'order_id': 'order_nébias_2025_06_18:22_36_57',
            'price': 'order_siqueira_campos_2025_06:18_22_36_57'
        }
    )
])
@freeze_time('2025-06-18 22:36:57')
def test_order(mocker, input_request, mock_database, expected):

    ...