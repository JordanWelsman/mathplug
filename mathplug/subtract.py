def subtract(*arg):
    """Returns result of subtraction of other arguments on first argument."""
    subtractor = 0
    for n in arg:
        subtractor += n
    return (arg[0] - (subtractor-arg[0]))