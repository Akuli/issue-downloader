from typing import Optional

def bar(var: str):
    pass

def foo(var: Optional[str]=None):
    var_not_None = not (var is None)
    if var_not_None:
        # var can only be a `str` at this point,
        # but `mypy` complains that
        # Argument 1 to "bar" has incompatible type "Optional[str]"; expected "str"
        bar(var)

def foo2(var: Optional[str]=None):
    if not(var is None):
        # no complaints from mypy
        bar(var)
