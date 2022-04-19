from typing import Union, overload
from typing_extensions import Literal

@overload
def f(*, flag: Literal[True]) -> float: ...
@overload
def f(*, flag: Literal[False] = False) -> str: ...
def f(*, flag: bool = False) -> Union[str, float]:
    return 5

reveal_type(f(flag=True))
reveal_type(f(flag=False))
reveal_type(f())
