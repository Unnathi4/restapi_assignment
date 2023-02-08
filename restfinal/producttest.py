import unittest
from unittest.mock import Mock,patch
from nose.tools import assert_is_not_none

from product import get_products,get_product


@patch('product.get_products')
def test_getting_products(mock_get):
    mock_get.return_value.ok = True
    response = get_products()
    assert_is_not_none(response)

@patch('product.get_product')
def test_getting_product(mock_get):
    mock_get.return_value.ok = True
    response = get_product("1")
    assert_is_not_none(response)

