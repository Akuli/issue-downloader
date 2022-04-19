from typing import TypeVar, Generic

T = TypeVar('T')
class A:
    def __init__(self, x: T) -> None:
        self.x = x
    def get(self) -> T:
        return self.x

x: int = A('lol').get()
