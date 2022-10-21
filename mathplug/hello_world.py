def hello_world(name=None):
    """Greets the caller."""
    greeting = ""
    if name is None:
        greeting = "Hello, World!"
    else:
        greeting = f"Hello, {name}!"
    return greeting

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_ihello_world_name():
    assert hello_world("Foo Bar") == "Hello, Foo Bar!"

def test_hello_world_wrong():
    assert hello_world() != "Something else"