from typing import TypeAlias

A: TypeAlias = "str"

isinstance(1, A)  # no error
reveal_type(A)  # type[str]
