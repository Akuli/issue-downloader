from typing import Optional, TypeVar, Any

T = TypeVar('T')

def not_none(obj: Optional[T]) -> T:
    assert obj is not None
    return obj

yy: Optional[Any] = "hello"

not_none(yy).upper()  # Mypy will complain here: `error: <nothing> has no attribute "parent"`
