def multiply(*arg):
    """Returns the product of arguments."""
    product = 1
    for n in arg:
        product *= n
    return product

print(multiply(20, 45, 12))