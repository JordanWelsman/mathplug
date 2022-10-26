# addition
def add(*arg):
    """Returns sum of numbers passed in."""
    total = 0
    for n in arg:
        total += n
    return total


# division
def divide(*arg):
    """Returns result of division of other arguments on first argument."""
    denominator = arg[0]
    numerators = arg[1:]
    result = []
    if (len(arg) > 2): # if more than 1 numerator is provided
        for x, n in enumerate(numerators): # iterate through numerators
            result.append(n / denominator) # divide by denominator, append to result
    else:
        result = numerators[0] / denominator # divide numerator by denominator, write to result
    return result


# Hello, World!
def hello_world(name=None):
    """Greets the caller."""
    greeting = ""
    if name is None:
        greeting = "Hello, World!"
    else:
        greeting = f"Hello, {name}!"
    return greeting


# multiplication
def multiply(*arg):
    """Returns the product of arguments."""
    product = 1
    for n in arg:
        product *= n
    return product


# square root
def square_root(arg):
    """Returns the root of the argument."""
    if arg < 0:
        return None
    return arg ** 0.5


# square
def square(arg):
    """Returns the argument multiplied by itself."""
    return arg * arg


# subtraction
def subtract(*arg):
    """Returns result of subtraction of other arguments on first argument."""
    subtractor = 0
    for n in arg:
        subtractor += n
    return (arg[0] - (subtractor-arg[0]))