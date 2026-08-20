from twttr import shorten

def test_normal():
    assert shorten('Twitter') == 'Twttr'

def test_mixed():
    assert shorten('twittEr') == 'twttr'

def test_upper():
    assert shorten('TWITTER') == 'TWTTR'

def test_number():
    assert shorten('TWITTER50') == 'TWTTR50'

def test_punctuation():
    assert shorten('TWITTER50,') == 'TWTTR50,'

