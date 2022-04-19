from typing import Any

def func() -> Any:
    ...

var = func()
reveal_type(var)  # Any
assert isinstance(var, bool)
reveal_type(var)  # bool

if var:
    reveal_type(var)  # Literal[True]
    pass
reveal_type(var)  # Any -> should still be 'bool'!
