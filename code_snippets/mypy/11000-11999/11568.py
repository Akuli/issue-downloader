# main.py
from drf_spectacular.utils import Direction


def go(direction: Direction) -> int:
    if direction == "request":
        return 1
    elif direction == "response":
        return 2

from drf_spectacular.drainage import (
    Final, Literal, error, get_view_method_names, isolate_view_method, set_override, warn,
)
...
Direction = Literal['request', 'response']

if sys.version_info >= (3, 8):
    from typing import Final, Literal, _TypedDictMeta  # type: ignore[attr-defined] # noqa: F401
else:
    from typing_extensions import (  # type: ignore[attr-defined] # noqa: F401
        Final, Literal, _TypedDictMeta,
    )

from typing import Literal

Direction = Literal['request', 'response']


def go(direction: Direction) -> int:
    if direction == "request":
        return 1
    elif direction == "response":
        return 2
