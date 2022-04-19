from typing import Union, Tuple

def def1(var: bool) -> Union[Tuple[str, str], Tuple[None, None]]:
    if var:
       return "", ""
    return None, None

def def2(var: bool) -> Union[Tuple[str, str], Tuple[None, None]]:
    a, b = def1(var)
    if var:
        return a, b
    return None, None
