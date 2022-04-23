# a.py
def add_int(a, b):
    return a + b

add_int("a", "b") # mypy does not complain, actually ignores the entire file

# a.pyi
def add_int(a:int, b:int) -> int: ...

# client.py
from a import add_int
add_int(1, 2)
add_int(1, "2") # here mypy is going to complain
