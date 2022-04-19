from typing import Union


def f(a: Union[str, int]):
    if a == 'a':
        reveal_type(a)  # expect str
        str.lower(a)
