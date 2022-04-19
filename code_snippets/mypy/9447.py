class Base:
    def a(self, a: int) -> None: ...

class Derived(Base):
    def a(self, _a: int) -> None:  ...

def foo(b: Base) -> None:
    b.a(a=1)

foo(Derived())
