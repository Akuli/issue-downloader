from typing import TypeVar

T = TypeVar("T")

def foo(t: type[T], data: str) -> None:
    if isinstance(data, t):
        print(data.__str__)  # error: <nothing> has no attribute "__str__"
