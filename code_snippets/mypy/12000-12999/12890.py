from abc import ABC, abstractmethod

class A(ABC):
    @property
    @abstractmethod
    def foo(self) -> str: ...

class B(A):
    def foo(self) -> str:
        return "asdf"

def get_foo(a: A) -> str:
    return a.foo

b = B()

# runtime error - AttributeError: 'function' object has no attribute 'capitalize'
get_foo(b).capitalize()
