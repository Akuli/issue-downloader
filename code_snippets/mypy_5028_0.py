# a.py
def add_int(a, b):
    return a + b

add_int("a", "b") # mypy does not complain, actually ignores the entire file
