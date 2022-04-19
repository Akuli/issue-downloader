# a.pyi
def a() -> None: ...

# b.pyi
def not_b() -> None: ...

# c.pyi
def c() -> None: ...

# __init__.pyi
from .a import *
from .b import *
from .c import c
