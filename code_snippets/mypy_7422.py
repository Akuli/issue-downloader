from typing import Tuple, Union

def x() -> Union[Tuple[int, int], Tuple[str, str]]:
    ...

a, b = x()

if isinstance(b, int):
    reveal_type(a) # can only be int but is reported as Union[int, str]

