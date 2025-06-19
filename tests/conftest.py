import pytest

from src.Models.Models import Payment, Order, Requisite, Food, Ingredient, Topping


@pytest.fixture
def mock_database(mocker):

    ...