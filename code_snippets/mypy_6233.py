if foo():
    x = 0
    # Type of x is 'int' here
else:
    x = ''  # No error here
    # Type of x is 'str' here
reveal_type(x)  # Union[int, str]
