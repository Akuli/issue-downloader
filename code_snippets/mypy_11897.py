from typing import Union

class A:
    x: Union[int, str] = 5

class B(A):
    x = 5

class C(B):
    # error: Incompatible types in assignment (expression has type "str", base class "B" defined the type as "int")
    x = "5"

class RefA:
    x: A

class RefB(RefA):
    x = B()

class RefC(RefB):
    # error: Incompatible types in assignment (expression has type "A", base class "RefB" defined the type as "B")
    x = A()
