from typing import Callable


class Parent:
    foo: Callable[[str], str] | str 


class Child1(Parent):
    foo = "bar"  # OK


class Child2(Parent):
    @staticmethod
    def foo(x: str) -> str:  # Signature of "foo" incompatible with supertype "Parent"
        return x.lower()
