from typing import Optional, Any

class A: ...

def anything() -> bool: ...
def getA() -> Any: ...
x: Optional[A]

reveal_type(x)  # N: Revealed type is "Optional[A]"

if (x := getA()) is not None:
    reveal_type(x)  # N: Revealed type is "Any"
reveal_type(x) # N: Revealed type is "Any"
