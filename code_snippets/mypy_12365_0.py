# mypy: always-true=foo
from typing import Literal

foo: bool

if not foo:
    print(1)  # no error ✅

bar: Literal[True]

if not bar:
    print(1)  # error: Statement is unreachable ✅
