from typing import _T

class A:...
class B(A):
    a: int
class C(A):
    a: int

def safe(it: _T | None) -> _T:...

b_or_c: B | C

value = safe(b_or_c)

reveal_type(value) #A, should be B | C
value.a # error
