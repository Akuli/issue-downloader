from typing import Callable, Optional

def f(func: Optional[Callable[[], None]] = None) -> None:
    if func is None:
        def func() -> None:
            pass

    func()
