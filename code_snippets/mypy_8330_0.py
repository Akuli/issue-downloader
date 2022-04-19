from typing import overload
from typing_extensions import Literal


class Cat:
    @overload
    def __new__(cls, name: Literal['Tabby']) -> 'Tabby': ...
    @overload
    def __new__(cls, name: Literal['Kitty']) -> 'Kitty': ...

    def __new__(cls, name: str) -> 'Cat': ...

class Kitty(Cat):
    pass

class Tabby(Cat):
    pass


reveal_type(Cat('Kitty'))
reveal_type(Cat('Tabby'))
