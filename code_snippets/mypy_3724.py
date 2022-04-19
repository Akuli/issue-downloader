from typing import Any, Optional

def foo() -> Optional[int]:
    return 42

raz: Any

def bar() -> int:
    x = foo()
    if isinstance(x, int):
        reveal_type(x)
        x = raz()
        reveal_type(x)
        x = x + 42
    return 0
