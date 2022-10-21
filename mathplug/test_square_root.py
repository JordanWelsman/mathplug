from mathplug import square_root as t

def test_square_root():
    assert t.square_root(16) == 4

def test_square_root_negative():
    assert t.square_root(-4) == None

def test_square_root_wrong():
    assert t.square_root(10) != 5