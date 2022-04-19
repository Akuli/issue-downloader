class A:
    def __init__(self):
        raise RuntimeError

from typing import NoReturn

class A:
    def __init__(self) -> NoReturn: ...

