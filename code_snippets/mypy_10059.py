from typing import Union

def f(v: Union[int, str]) -> str:
    if isinstance(v, str):
        try:
            v = int(v)
        except ValueError:
            # return as is
            return v
    return str(v)
