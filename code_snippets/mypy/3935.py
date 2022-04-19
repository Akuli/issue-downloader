from typing import cast, List, Union

Scalar = Union[str, float]


def good() -> List[Scalar]:
    return ["foo", 1.0]


def bad(params: List[Scalar]) -> List[Scalar]:
    # error: Incompatible return value type (got List[object], expected
    # List[Union[str, float]])
    # error: Unsupported operand types for + (List[object] and
    # List[Union[str, float]])
    return ["foo", 1.0] + params


def good2(params: List[Scalar]) -> List[Scalar]:
    return cast(List[Scalar], ["foo", 1.0]) + params
