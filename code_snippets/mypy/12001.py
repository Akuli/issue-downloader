from copy import deepcopy
from typing import Literal, Union

def f(a: str, b: bool) -> Union[Literal[True], str]:
    return b or deepcopy(a)

print(f("abc", False))
print(f("abc", True))
