import unittest
from unittest.mock import Mock,patch
from nose.tools import assert_is_not_none

from app import get_customers,get_customer


@patch('app.get_customers')
def test_getting_customers(mock_get):
    mock_get.return_value.ok = True
    response = get_customers()
    assert_is_not_none(response)

@patch('app.get_customer')
def test_getting_customer(mock_get):
    mock_get.return_value.ok = True
    response = get_customer("ALFKI")
    assert_is_not_none(response)

'''@patch('product.get_products')
def test_getting_products(mock_get):
    mock_get.return_value.ok = True
    response = get_products()
    assert_is_not_none(response)'''

