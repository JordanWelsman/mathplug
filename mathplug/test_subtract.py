from mathplug import subtract as t

def test_subtract():
    assert t.subtract(20, 10) == 10

def test_subtract_multiple():
    assert t.subtract(50, 10, 20) == 20

def test_subtract_wrong():
    assert t.subtract(30, 15) != 20