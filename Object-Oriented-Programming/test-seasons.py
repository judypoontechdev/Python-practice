from seasons import transfer
import pytest

def test_format():
    with pytest.raises(SystemExit):
        transfer('19th February 2002')
    with pytest.raises(SystemExit):
        transfer('19-02-2002')

def test_range():
    with pytest.raises(ValueError):
        transfer('2004-13-30')

def test_outcome():
    assert transfer('2025-08-27') == 'Five hundred twenty-five thousand, six hundred minutes'
