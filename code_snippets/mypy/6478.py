from typing import List, Union


def f(x: Union[int, List[int]]) -> None:  # `TypeVar` can fix it
    x + x
