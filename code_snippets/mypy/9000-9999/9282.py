from typing import TypeVar, Type

T = TypeVar("T", bound="A")

class A:
    @classmethod
    def foo(cls: Type[T]) -> T:
        print(cls.__qualname__)
        return cls()

class B(A):
    @classmethod
    def foo(cls: Type[T]) -> T:
        return super().foo()

B.foo()
