from typing import Callable
from mypy_extensions import Arg

x: Callable[[Arg(int, 'foobar'), Arg(int, 'bir'), Arg(int, 'fubar')], None]
y: Callable[
    [Arg(int, 'foobar'), Arg(int, 'blr'), Arg(int, 'fubar')], None]

x = y
