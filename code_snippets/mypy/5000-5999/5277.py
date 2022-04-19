T = TypeVar('T')
class Fooable(Protocol):
    def foo(self: T, a: T) -> int:
        ...
class A:
    a = 1
    def foo(self, a: 'A') -> int:
        return self.a + a.a
class B:
    b = 1
    def foo(self, b: 'B') -> int:
        return self.b + b.b
def foo(a: Fooable, b: Fooable) -> None:
    a.foo(b)
foo(A(), B())
