from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar._capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == '🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar._size == 2

    with pytest.raises(ValueError):
        jar.deposit(14)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    assert jar._size == 1

    with pytest.raises(ValueError):
        jar.withdraw(2)