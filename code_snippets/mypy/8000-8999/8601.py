from decimal import Decimal
from typing import Union

def check(x: Decimal, y: Union[Decimal, int]) -> bool:
    return x < -abs(y)
