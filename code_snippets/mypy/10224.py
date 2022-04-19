from typing import Any, Union
class A: ...
class B: ...
class C: ...

def _binary_operation(left: C, right: Union[A, B]) -> Any: ...

ALL = Union[A, B, C]
def commutative_binary_operation(left: ALL, right: ALL) -> Any:
    # Handling of a corner case.
    if isinstance(left, C) and isinstance(right, C):
        ...
    elif isinstance(left, C):
        reveal_type(right)
        return _binary_operation(left, right)
    elif isinstance(right, C):
        reveal_type(left)
        return _binary_operation(right, left)

    # Treatment of other combination of types.
    ...
