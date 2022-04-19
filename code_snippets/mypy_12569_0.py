from typing import Callable


class Parent:
    foo: Callable[[str], str]

class Child2(Parent):
    @staticmethod
    def foo(x: str) -> str:
        return x.lower()
