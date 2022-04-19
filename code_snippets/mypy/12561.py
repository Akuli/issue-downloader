from typing import Any, Callable


class Foo:
    def __init__(self, a: int) -> None:
        print(a)


def bar(f: Callable[[Any], Any]) -> None:
    if type(f) ==Foo:
        print("The same!")

    f(3)


bar(Foo)
