from typing import NamedTuple

class NTup1(NamedTuple):
    a: bool

class NTup2(NTup1):   # Should be an error
    b: bool

tup = NTup2(a=True, b=False)  # Python: TypeError: <lambda>() got an unexpected keyword argument 'b'
                              # Mypy: error: Unexpected keyword argument "b" for "NTup2"

tup = NTup2(a=True)  # Works in Python

tup.b   # Python: AttributeError: 'NTup2' object has no attribute 'b'
# but mypy thinks the `b` field exists
reveal_type(tup.b)  # Mypy: note: Revealed type is "builtins.bool"

