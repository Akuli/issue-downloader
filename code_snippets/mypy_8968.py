# test.py
from package import E
name = 'a'
val = E[name]
assert val == E.a

# package/__init__.pyi
import package.test_def
E = package.test_def.E

# package/test_def.py
from enum import Enum

class E(Enum):
    a = 'a'
    b = 'b'
    c = 'c'

