import enum

class A(enum.Enum):
    X = 'x'

def f(v: A):
    pass

f(A.X)
