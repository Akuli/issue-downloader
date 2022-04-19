import sys
from typing import Any, Mapping, Type, TypeVar, cast

import typeguard

TD = TypeVar('TD')

def check_typed_dict(value: Mapping[Any, Any], expected_type: Type[TD]) -> TD:
    """
    Validates the given dict against the given TypedDict class, and wraps the value as the given TypedDict type.

    This is a shortcut to :func:`typeguard.check_typed_dict()` function to fill extra information
    """
    assert issubclass(expected_type, dict) and hasattr(expected_type, '__annotations__'), \
           f"expected_type ({type(expected_type)}) must be a TypedDict class"
    frame = sys._getframe(1)
    _globals = frame.f_globals
    _locals = frame.f_locals
    memo = typeguard._TypeCheckMemo(_globals, _locals)
    typeguard.check_typed_dict('value', value, expected_type, memo)
    # Here we passed the check, so return it after casting.
    return cast(TD, value)

