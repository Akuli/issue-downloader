# mypy: allow-redefinition
from random import random

def f() -> None:
    x = 0

    reveal_type(x)
    print(x)

    def f2() -> float:
        return random()

    x = 'x'
    reveal_type(x)
