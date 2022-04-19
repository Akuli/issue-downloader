from typing import Any, Callable, List, Mapping, Tuple, TypeVar

U = TypeVar('U', bound=Mapping[str, Any])


def f(dict_factory: Callable[[List[Tuple[str, Any]]], U] = dict) -> U:
    return dict_factory([('a', 1)])
