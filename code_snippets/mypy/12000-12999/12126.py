from typing import Callable, Any, TypeVar

T = TypeVar('T', bound='BaseClass')  # Alternative Example

class BaseClass:
    def default_example(self) -> list[int]:
         return [1, 2, 3]
    
    example: Callable[[Any], list[int]] | list[int] = default_example

class ChildClassA(BaseClass):
    example: list[int] = [1, 2, 3]
    
class ChildClassB(BaseClass):
    example = lambda self: [1,2,3]

class ChildClassC(BaseClass):
    def default_example(self) -> list[int]:
         return [1, 2, 3]
    example = default_example

class ChildClassD(BaseClass):
    def example(self) -> list[int]:
         return [1, 2, 3]
