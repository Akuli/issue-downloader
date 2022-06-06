class A:
    f: object

class B(A):
    f: float

b = B()

a: A = b
a.f = "abc"

b.f.is_integer()
