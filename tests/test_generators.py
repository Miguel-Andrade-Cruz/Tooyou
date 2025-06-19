import pytest
from unittest.mock import patch
from datetime import datetime
from freezegun import freeze_time

from src.Tools.generators import generate_order_id


@freeze_time("2025-06-15 14:35:37")
@patch('src.Tools.generators.datetime.now')
def test_generate_order_id(mock):

    expected_order_id = 'order_test_client_one_2025_06_15:14_35_37'
    mock.return_value = datetime(2025, 6, 15, 14, 35, 37)

    client_name = 'Test Client One'

    result = generate_order_id(client_name)
    
    assert result == expected_order_id, f"Expected {expected_order_id}, but got {result}"
