from typing import Any

from non_existent import f  # type: ignore  # Not in the build

def g(): pass

def h() -> None:
    g(asdf=1)  # Error: Call to untyped function "g" in typed context
    f(asdf=1)  # No error reported, but this is untyped
    ff: Any
    ff()  # No error reported, and again this in untyped
