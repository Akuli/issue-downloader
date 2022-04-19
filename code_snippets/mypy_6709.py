class A:
    def f(self, x: int) -> None:
      print("A: ", x)

class B(A):
    def f(self, x: int) -> None:
      print("B: ", x)

class C(A):
    def f(self, n: int) -> None:
      print("C: ", n)

a = A()
a.f(x=3)

b = B()  # type: A
b.f(x=3)

c = C()  # type: A
c.f(x=3)  # mypy passes, but gives runtime error: TypeError: f() got an unexpected keyword argument 'x'

c2 = C()  # type: A
c2.f(n=3) # mypy gives an error:  error: Unexpected keyword argument "n" for "f" of "A"   but runtime works.

c3 = C()  # type: C
c3.f(x=3)    # mypy give type error: error: Unexpected keyword argument "x" for "f" of "C", and runtime error: mypy-issue.py:25: error: Unexpected keyword argument "x" for "f" of "C"

c4 = C()  # type: C
c4.f(n=3)  # no errors in mypy or at runtime
