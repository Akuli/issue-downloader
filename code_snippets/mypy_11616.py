from typing import Literal

def page(page: Literal["p1", "p2"]): ...

def foo(num: Literal["1", "2"]):
    page(f"p{num}")
    page("p" + num)
    page("p" + "1")
