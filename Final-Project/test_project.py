import pytest
import os
from cs50p.project.project import validate_float, validate_string, get_previous_total

def test_validate_float():
    assert validate_float('22') == 22.0
    assert validate_float('123.45') == 123.45

    with pytest.raises(ValueError):
        validate_float('cat')

def test_validate_string():
    assert validate_string('Stocks') == 'Stocks'

def test_get_previous_total():
    if os.path.exists('finance.csv'):
        os.remove('finance.csv')

    assert get_previous_total() == 0.0
