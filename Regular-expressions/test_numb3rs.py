from numb3rs import validate

def test_bigger():
    assert validate('300.1.1.1') == False
    assert validate('256.255.1.1') == False
    assert validate('1.300.1.1') == False
    assert validate('1.1.300.1') == False
    assert validate('1.1.1.300') == False

def test_smaller():
    assert validate('-1.1.1.1') == False

def test_normal():
    assert validate('1.1.1.1') == True
    assert validate('255.255.255.255') == True

def test_numbers():
    assert validate('1.1.1.1.1') == False
    assert validate('255.255.255') == False

