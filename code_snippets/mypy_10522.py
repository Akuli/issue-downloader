from typing import Protocol, runtime_checkable

@runtime_checkable
class Foo(Protocol):
    class Bar:
        pass
