# mypy: always-true=foo
from typing import Literal

foo: bool

if not foo:
    print(1)  # no error ✅

bar: Literal[True]

if not bar:
    print(1)  # error: Statement is unreachable ✅

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

