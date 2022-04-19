from typing import TypeVar

T = TypeVar('T')

class X:
    def __init__(self: T):
        super().__init__() # error: Argument 2 for "super" not an instance of argument 1
