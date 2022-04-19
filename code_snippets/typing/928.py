from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from foo.bar import Baz

def foo(baz: Baz):
    print(baz.bat)
