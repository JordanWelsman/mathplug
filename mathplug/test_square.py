from mathplug import square as t

def test_square():
    assert t.square(4) == 16

def test_square_negative():
    assert t.square(-10) == 100

def test_square_wrong():
    assert t.square(3) != 6