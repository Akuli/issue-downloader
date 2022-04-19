from typing import Callable

def dec(f) -> Callable[[int], None]: pass

x = int()
if x:
    def f(x: str) -> None: pass
else:
    # No complaint about incompatible redefinition!
    @dec
    def f(): pass
