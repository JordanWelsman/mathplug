from tokenize import Number


def add(*arg):
    """Returns sum of numbers passed in."""
    total = 0
    for n in arg:
        total += n
    return total

print(add(1, 2))