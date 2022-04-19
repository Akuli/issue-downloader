from typing import Protocol, cast

class FooType(Protocol):
    def __call__(self, ham: str) -> str:
        pass

def foo(ham: str) -> str:
    pass


v = cast(FooType, foo)
u: FooType = foo
