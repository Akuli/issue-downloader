from typing import Any
b: Any
def foo(a: Any):
    if isinstance(a, (str, b)):
        return True
    return False  # Statement is unreachable
