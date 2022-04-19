from typing import cast

class Test:
    a: int
    
t = Test()

cast(t.a, int)  # error: Name "t.a" is not defined
