class A:
    x: str
    def x(self) -> str: ...

class B:
    x: int
    def x(self) -> int: ...

class C(A, B): ...
