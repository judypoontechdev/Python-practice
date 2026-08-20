import pytest
from fuel import convert
from fuel import gauge

def test_convert_floats():
    with pytest.raises(ValueError):
        convert('3.5/4.5')

def test_convert_slash():
    with pytest.raises(ValueError):
        convert('34')

def test_convert_special():
    with pytest.raises(ValueError):
        convert('cat')

def test_convert_number():
    assert convert('3/4') == 75

    with pytest.raises(ValueError):
        convert('4/3')

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert('4/0')

def test_convert_negative():
    with pytest.raises(ValueError):
        convert('-2/4')

def test_gauge_one():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'

def test_gauge_ninetynine():
    assert gauge(99) == 'F'

def test_gauge_others():
    assert gauge(50) == '50%'
