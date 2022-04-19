# test.py
from typing import (NamedTuple, Generic, TypeVar)

class _S:
    pass

S = TypeVar('S', bound='_S')

class A(NamedTuple, Generic[S]):
    s: S
