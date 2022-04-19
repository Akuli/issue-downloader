from typing import Iterable
from typing import List
from typing import MutableSequence
from typing import Union
from typing import overload


class RecordBehaviourList(MutableSequence[str]):
    def __init__(self, lst: List[str]) -> None:
        self._lst = lst

    @overload
    def __getitem__(self, index: int) -> str:
        ...

    @overload  # noqa: F811  # TODO: flake8 3.8
    def __getitem__(self, index: slice) -> MutableSequence[str]:
        ...

    def __getitem__(  # noqa: F811  # TODO: flake8 3.8
            self,
            index: Union[int, slice],
    ) -> Union[str, MutableSequence[str]]:
        return self._lst[index]

    @overload
    def __setitem__(self, index: int, value: str) -> None:
        ...

    @overload  # noqa: F811  # TODO: flake8 3.8
    def __setitem__(self, index: slice, value: Iterable[str]) -> None:
        ...

    def __setitem__(  # noqa: F811  # TODO: flake8 3.8
            self,
            index: Union[int, slice],
            value: Union[str, Iterable[str]],
    ) -> None:
        self._lst[index] = value

    def __delitem__(self, index: Union[int, slice]) -> None:
        del self._lst[index]

    def insert(self, index: int, value: str) -> None:
        self._lst.insert(index, value)
