import warnings
from typing import NoReturn

def foo() -> NoReturn:
    warnings.warn("this is deprecated", DeprecationWarning)
    raise NotImplementedError

foo()  # I would expect a warning here
