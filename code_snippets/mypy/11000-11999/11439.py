import warnings
from typing import NoReturn

def foo() -> NoReturn:
    warnings.warn("this is deprecated", DeprecationWarning)
    raise NotImplementedError

foo()  # I would expect a warning here

class A:
    def foo(self) -> None:
        print()

class B(A):
    def foo(self) -> NoReturn:
        warnings.warn("this is an unsupported operation", DeprecationWarning)
        raise NotImplementedError()


B().foo()  # I would like a warning that this is unsupported

