from typing import Any, Mapping, MutableMapping


def test_mutablemapping(obj: Mapping[Any, Any]) -> MutableMapping[Any, Any]:
    if issubclass(type(obj), MutableMapping):
        return obj  # error: Incompatible types in assignment (expression has type "Mapping[Any, Any]", variable has type "MutableMapping[Any, Any]")
    else:
        return dict(obj)

from typing import Any, Mapping, MutableMapping


def test_mutablemapping2(obj: Mapping[Any, Any]) -> MutableMapping[Any, Any]:
    if isinstance(obj, MutableMapping):
        return obj
    else:
        return dict(obj)

