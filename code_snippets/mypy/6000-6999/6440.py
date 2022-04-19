from typing import Callable, Iterable, Mapping, MutableMapping, TypeVar, List, cast

T = TypeVar('T')
Tk = TypeVar('Tk')
Tv = TypeVar('Tv')

def group_by(
    items: Iterable[T],
    *,
    key: Callable[[T], Tk],
    value: Callable[[T], Tv] = lambda x: cast(Tv, x),
) -> Mapping[Tk, Iterable[Tv]]:
    result: MutableMapping[Tk, List[Tv]] = {}
    for item in items:
        result.setdefault(key(item), []).append(value(item))

    return result
