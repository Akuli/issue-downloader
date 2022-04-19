class A:
    x: float

class B(A):
    x: int  # no error, though unsafe

def f(a: A) -> None:
    a.x = 1.1

b = B()
f(b)
b.x  # float at runtime, though declared as int
