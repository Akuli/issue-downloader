import attr

from typing import Union

@attr.s
class A:
    left: 'B' = attr.ib()
    right: 'B' = attr.ib()

B = Union[list, str]

def foo() -> A:
    # return A(left=5, right=[])
    return A(left=[], right=5)
