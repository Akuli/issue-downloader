# _collections_abc.pyi
@StubOnlyBase(KeysView[_KT_co], Generic[_KT_co, _VT_co])
class dict_keys:
    ...

# builtins.pyi
@StubOnlyBase(numbers.Integral)
class int:
    ...

from typing import _alias  # type: ignore[attr-defined]
from typing import TYPE_CHECKING
from _collections_abc import dict_keys

if not TYPE_CHECKING:
    dict_keys = _alias(dict_keys, 2)

def foo(dk: dict_keys[str, int]) -> None: ...
