from typing import TypedDict, List


class Dct(TypedDict):
    x: int


def foo() -> List[Dct]:
    return [{"x": 3}]
