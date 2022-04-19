from typing import Any, Iterable, Mapping


def foo(foo: Iterable[Mapping[str, Any]]) -> None:
    pass


foo(({},))
