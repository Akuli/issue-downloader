from typing import TypeAlias

Recursive: TypeAlias = str | list["Recursive"]

def foo(r: Recursive) -> None:
    if not isinstance(r, str):
        foo(r[0])
    if not isinstance(r, list):
        r.casefold()

foo("")
foo(list[""])
foo(list[list[""], ""])
