from typing import Tuple, TypeVar
import collections

N = collections.namedtuple("N", "name")
T = TypeVar("T", N, Tuple[N, N])
# T = TypeVar("T", N, Tuple[N, ...])


def get_name_bad(item: T) -> str:
    return item.name if isinstance(item, N) else item[0].name


def get_name_good(item: T) -> str:
    if isinstance(item, N):
        return item.name
    return item[0].name


foo = N("1")
bar = N("2")
both = (foo, bar)

get_name_good(foo)
get_name_good(bar)
get_name_good(both)

get_name_bad(foo)
get_name_bad(bar)
get_name_bad(both)


