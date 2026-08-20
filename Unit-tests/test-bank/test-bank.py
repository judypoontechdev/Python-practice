from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('HELLO') == 0

def test_startwithletterh():
    assert value('hey') == 20
    assert value('how are you?') == 20

def test_otherwise():
    assert value('weather seems nice!') == 100


