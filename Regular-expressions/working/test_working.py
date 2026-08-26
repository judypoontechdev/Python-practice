import pytest
from working import convert

def test_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('9AM to 5PM')

def test_range():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

def test_edge_cases():
    assert convert('12 AM to 5 PM') == '00:00 to 17:00'
    assert convert('12 PM to 5 PM') == '12:00 to 17:00'

def test_inputs():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == '09:00 to 17:00'
    