from __future__ import annotations
from typing import Optional

class C1(object):
    def foo(self, a: C, b: C) -> None:
        reveal_type(a)  # Optional[C1]
        reveal_type(b)  # Any

    def bar(self, a: C) -> C:
        reveal_type(a)  # Optional[C1]
        return a

    def baz(self) -> C:
        return C()

C = Optional[C1]
        
def main() -> None:
    reveal_type(C1().foo)  # def (a: Optional[C1], b: Any)
    reveal_type(C1().bar)  # def (a: Optional[C1]) -> Any
    reveal_type(C1().baz)  # def () -> Optional[C1]
