from mathplug import add as t

def test_add():
    assert t.add(10, 20) == 30

def test_add_multiple():
    assert t.add(5, 10, 15) == 30

def test_add_wrong():
    assert t.add(30, 50) != 70