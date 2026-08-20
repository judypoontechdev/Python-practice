from plates import is_valid

def test_letters():
    assert is_valid('CS50') == True
    assert is_valid('C50') == False

def test_length():
    assert is_valid('CS5050') == True
    assert is_valid('CS5050505050') == False

def test_number():
    assert is_valid('AAA222') == True
    assert is_valid('CS50AA') == False

def test_zero():
    assert is_valid('CS05') == False

def test_special_characters():
    assert is_valid('__CS50') == False
    assert is_valid('CS__50') == False
    assert is_valid(' *C*5*') == False
