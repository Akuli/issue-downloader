from typing import Callable, Union
from mypy_extensions import Arg

def f(x: Callable[[Arg(int, 'x')], None]) -> None: pass

y: Callable[[Union[int, str]], None]
f(y)  # error
