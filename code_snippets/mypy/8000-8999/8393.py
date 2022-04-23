from typing import List, Union, overload
from typing_extensions import final


class Foo:
    @overload
    def get(self, index: int) -> int:
        ...

    @overload  # noqa: F811
    def get(self, index: slice) -> List[int]:
        ...

    def get(self, index: Union[int, slice]) -> Union[int, List[int]]:  # noqa: F811
        ...


class Bar(Foo):
    @overload
    def get(self, index: int) -> int:
        ...

    @overload  # noqa: F811
    def get(self, index: slice) -> List[int]:
        ...

    @final  # noqa: F811
    def get(self, index: Union[int, slice]) -> Union[int, List[int]]:
        if isinstance(index, int):
            return 3
        elif isinstance(index, slice):
            return [3, 4, 5]
        else:
            raise TypeError(...)

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
