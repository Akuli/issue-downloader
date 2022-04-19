from typing import List, TypeVar, Union

_T = TypeVar("_T")


def func(param: Union[List[_T], List[List[_T]]]) -> _T:
    ...

func([1])
func([[1]])
