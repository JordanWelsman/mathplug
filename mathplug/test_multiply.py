from mathplug import multiply as t

def test_multiply():
    assert t.multiply(5, 4) == 20

def test_multiply_multiple():
    assert t.multiply(7, 3, 2) == 42

def test_multiply_wrong():
    assert t.multiply(6, 2) != 8