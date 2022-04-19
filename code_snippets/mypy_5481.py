class Descr:
    def __get__(self, inst: Any, owner: Any) -> int: ...

class Proto(Protocol):
    x: int

class C:
    x = Descr()

a: Proto = C()
