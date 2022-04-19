from typing import TypeVar
from typing_extensions import Protocol

TA = TypeVar("TA", contravariant=True)

class P(Protocol[TA]):
    def __call__(self, *, a: TA, b: int) -> None: ...

def misordered(*, b: int, a: TA) -> None: ... # Should be seen as Protocol[TA]
def ordered(*, a: TA, b: int) -> None: ...      # Should be seen as Protocol[TA]
def explicit(*, b: int, a: str) -> None: ...    # Should be seen as Protocol[str]
    
    
def supports_protocol_int(a: P[int]) -> None: ... 
def supports_protocol_str(a: P[str]) -> None: ...
    
supports_protocol_int(misordered) # Works, since TA = int does not cause problem
supports_protocol_str(misordered) # BUG: Does not work. TA is determined to be int.
supports_protocol_int(ordered)    # Works.
supports_protocol_str(ordered)    # Works.
supports_protocol_int(explicit)   # Returns an error (as expected)
supports_protocol_str(explicit)   # Works.
