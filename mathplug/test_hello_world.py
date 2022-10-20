from mathplug import hello_world as t

def test_hello_world():
    assert t.hello_world() == "Hello, World!"

def test_hello_world_name():
    assert t.hello_world("Foo Bar") == "Hello, Foo Bar!"

def test_hello_world_wrong():
    assert t.hello_world() != "Something else"