from um import count

def test_start():
    assert count('Um, thanks for the album') == 1

def test_capital():
    assert count('UM, you alright?') == 1

def test_words():
    assert count('Mum, how are you um today?') == 1

def test_multiple():
    assert count('Um, um, umm, how are you?') == 2
