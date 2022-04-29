from __future__ import annotations
from functools import partialmethod

class A:
    def my_add(self, other: A, reverse: bool) -> A:
        return self

    __add__ = partialmethod(my_add, reverse=False)

a = A()
aa = A()
aaa = A()
result = sum([aa, a], start=aaa)
