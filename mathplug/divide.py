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