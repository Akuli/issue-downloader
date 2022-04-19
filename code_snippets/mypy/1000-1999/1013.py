class A:
    def f(self, x): ...
class B(A):
    def f(self, xx): ...

def f(a: A) -> None:
    a.f(x=1)  # Failure if a is an instance of B

f(B())
