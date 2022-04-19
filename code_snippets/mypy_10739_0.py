from decimal import Decimal
from typing import Union

def f(elem: Union[int, str, Decimal]) -> None:
    if isinstance(elem, int):
        return

    for _ in range(3):
        if isinstance(elem, (Decimal, int)) and elem > 10:
            continue
        reveal_type(elem)

    return None

