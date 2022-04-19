from typing import NamedTuple

class NTup1(NamedTuple):
    a: bool

class NTup2(NTup1):   # Should be an error
    b: bool
