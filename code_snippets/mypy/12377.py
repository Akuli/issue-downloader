[mypy]
follow_imports=skip
follow_imports_for_stubs=True

import enum

class A(enum.Enum):
    X = 'x'

def f(v: A):
    pass

f(A.X)

