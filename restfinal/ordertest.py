import unittest
from unittest.mock import Mock,patch
from nose.tools import assert_is_not_none

from order import get_orders,get_order


@patch('order.get_orders')
def test_getting_orders(mock_get):
    mock_get.return_value.ok = True
    response = get_orders()
    assert_is_not_none(response)

@patch('order.get_order')
def test_getting_order(mock_get):
    mock_get.return_value.ok = True
    response = get_order("10248")
    assert_is_not_none(response)
