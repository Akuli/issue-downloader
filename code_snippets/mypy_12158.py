from typing import final

@final
class A:
    b: int

if A():
    print("hi")  # no unreachable error

print(A() and "hi")

from typing import final

@final
class A:
    b: int
    
a: A | None
r1: int | None = a.b if a else None
r2: int | None = a and a.b  # error: Incompatible types in assignment (expression has type "Union[A, None, int]", variable has type "Optional[int]")

