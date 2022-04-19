from typing import Any, Union

class getter:
    def __get__(self, instance: "X1", owner: Any) -> str:
        return ""

class X1:
    prop = getter()

class X2:
    def __init__(self) -> None:
        self.prop = ""

def foo(x: Union[X1, X2]) -> None:
    x.prop
