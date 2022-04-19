from typing import Protocol

class Foo(Protocol):
    def __init__(self) -> None:  pass

Foo()  # disallowed


class ConcreteFoo(Foo):
    ...

ConcreteFoo()  # allowed
