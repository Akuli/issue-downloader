from typing import List, Union, overload
from abc import ABC, abstractmethod


class Foo(ABC):
    @overload
    def get(self, index: int) -> int:
        ...

    @overload  # noqa: F811
    def get(self, index: slice) -> List[int]:
        ...

    @abstractmethod  # noqa: F811
    def get(self, index: Union[int, slice]) -> Union[int, List[int]]:
        ...


class Bar(Foo):
    @overload
    def get(self, index: int) -> int:
        ...

    @overload  # noqa: F811
    def get(self, index: slice) -> List[int]:
        ...

    @abstractmethod  # noqa: F811
    def get(self, index: Union[int, slice]) -> Union[int, List[int]]:
        if isinstance(index, int):
            return 3
        elif isinstance(index, slice):
            return [3, 4, 5]
        else:
            raise TypeError(...)
