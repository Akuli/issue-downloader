# typed_dict_test.py
from typing import TypedDict

class D(TypedDict):
    a: str
    b: int


d_untyped = {"a": "foo", "b": 1}

d0 = D({"a": "foo", "b": 1})  # The only one that works
print(d0)

d1 = D(d_untyped)
print(d1)

d2 = D(**d_untyped)
print(d2)

d3 = D(dict(d_untyped))
print(d3)

d4 = D(dict(**d_untyped))
print(d4)
