from typing import Any, Mapping, MutableMapping


def test_mutablemapping2(obj: Mapping[Any, Any]) -> MutableMapping[Any, Any]:
    if isinstance(obj, MutableMapping):
        return obj
    else:
        return dict(obj)
