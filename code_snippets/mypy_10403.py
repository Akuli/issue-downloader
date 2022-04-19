from typing import Protocol

class A(Protocol):
    __name__: str
    def __call__(self) -> None: ...

def f() -> None: ...

reveal_type(f.__name__)  # note: Revealed type is 'builtins.str'
a: A = f  # error: Incompatible types in assignment (expression has type "Callable[[], None]", variable has type "A")  [assignment]
