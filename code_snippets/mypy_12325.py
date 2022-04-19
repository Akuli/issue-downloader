from typing import Literal


def foo(a: Literal[True]) -> None:
    ...


FOO: bool
foo(FOO)  # error: Argument 1 to "foo" has incompatible type "bool"; expected "Literal[True]"  [arg-type]
reveal_type(FOO)  # note: Revealed type is "builtins.bool"
if not FOO:
    pass
reveal_type(FOO)  # note: Revealed type is "Literal[True]"
if not FOO:
    pass
import test2

from test import FOO

reveal_type(FOO)  # note: Revealed type is "builtins.bool"
if FOO:
    pass
reveal_type(FOO)  # note: Revealed type is "Literal[True]"

