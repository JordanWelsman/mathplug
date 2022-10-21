from mathplug import divide as t

def test_divide():
    assert t.divide(10, 20) == 2

def test_divide_multiple():
    assert t.divide(5, 10, 15) == [2, 3]

def test_divide_wrong():
    assert t.divide(30, 60) != 3