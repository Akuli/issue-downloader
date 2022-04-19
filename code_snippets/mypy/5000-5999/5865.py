from typing import Any

a: Any
class C(a): pass  # Ok

def f(b: Any) -> None:
    class D(b): pass  # Errors: Invalid type "b"; Invalid base class

def g(c: Any) -> None:
    d: Any = c
    class E(d): pass  # Ok
