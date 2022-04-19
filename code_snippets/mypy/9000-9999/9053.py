from typing import Union, Callable, Type


# similar to a get-only property
class MyProperty:
    def __init__(self, func: Callable[['B'], int]) -> None:
        self.func = func

    def __get__(self, instance: 'B', owner: Type['B']) -> int:
        return self.func(instance)


# This class has an attribute 'x'
class A:
    def __init__(self) -> None:
        self.x = 123


# This class has a property 'x'
class B:
    @MyProperty
    def x(self) -> int:
        return 456


def foo(a: Union[A, B]) -> int:
    return a.x  # mypy detects an error here
