from typing import Any
import x  # this will be of type Any as ignore-missing-imports is True

class A(x):
    def __init__(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        self.a = 1

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()

reveal_type(a)
reveal_type(b)
reveal_type(c)

