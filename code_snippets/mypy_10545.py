# a.pyi

def foo() -> str: ...

# b.pyi

from a import *

def foo() -> int: ...  # type: ignore

