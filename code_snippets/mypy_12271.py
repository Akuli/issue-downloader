from typing import TypedDict

class A(TypedDict):
    x: int
a: A
a.setdefault('x', '')  # test.py:6:1: error: Argument 2 to "setdefault" of "TypedDict" has incompatible type "str"; expected "int"
