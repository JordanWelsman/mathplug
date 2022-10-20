def hello_world(name=None):
    """Greets the caller."""
    if name is None:
        print("Hello, World!")
    else:
        print(f"Hello, {name}!")