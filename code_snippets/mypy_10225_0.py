from typing import Union, Tuple

def def1(var: bool) -> Union[Tuple[str, str], Tuple[None, None]]:
    a, b = "", ""
    if var:
        return a, b
    return None, None
