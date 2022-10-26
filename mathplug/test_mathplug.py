# import module
from mathplug import mathplug as t


# add()
def test_add():
    assert t.add(10, 20) == 30

def test_add_multiple():
    assert t.add(5, 10, 15) == 30

def test_add_wrong():
    assert t.add(30, 50) != 70


# divide()
def test_divide():
    assert t.divide(10, 20) == 2

def test_divide_multiple():
    assert t.divide(5, 10, 15) == [2, 3]

def test_divide_wrong():
    assert t.divide(30, 60) != 3


# hello_world()
def test_hello_world():
    assert t.hello_world() == "Hello, World!"

def test_hello_world_name():
    assert t.hello_world("Foo Bar") == "Hello, Foo Bar!"

def test_hello_world_wrong():
    assert t.hello_world() != "Something else"


# multiply()
def test_multiply():
    assert t.multiply(5, 4) == 20

def test_multiply_multiple():
    assert t.multiply(7, 3, 2) == 42

def test_multiply_wrong():
    assert t.multiply(6, 2) != 8


# square_root()
def test_square_root():
    assert t.square_root(16) == 4

def test_square_root_negative():
    assert t.square_root(-4) == None

def test_square_root_wrong():
    assert t.square_root(10) != 5


# square()
def test_square():
    assert t.square(4) == 16

def test_square_negative():
    assert t.square(-10) == 100

def test_square_wrong():
    assert t.square(3) != 6


# subtract()
def test_subtract():
    assert t.subtract(20, 10) == 10

def test_subtract_multiple():
    assert t.subtract(50, 10, 20) == 20

def test_subtract_wrong():
    assert t.subtract(30, 15) != 20