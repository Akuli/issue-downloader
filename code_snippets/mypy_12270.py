from typing import TypedDict

class A(TypedDict):
    x: int
a: A
a.__setitem__('x', '')  # no error
b: int = a.__getitem__('x')  # error: Incompatible types in assignment (expression has type "object", variable has type "int")
