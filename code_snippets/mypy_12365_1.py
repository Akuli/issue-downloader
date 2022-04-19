# mypy: always-true=foo
from typing import Literal

foo: bool

def f1() -> None:
    if foo:
        return
    print(1)  # error: Statement is unreachable ❌

bar: Literal[True]

def f2() -> None:
    if bar:
        return
    print(1)  # error: Statement is unreachable ✅
