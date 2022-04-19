from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast, TYPE_CHECKING


def test(one: int | None = None, **kwargs: Any) -> int | None:
    print(repr(kwargs))
    return one


if TYPE_CHECKING:
    reveal_type(test)
    reveal_type(test())
    reveal_type(test(test='one'))
    reveal_type(test(**{'test': 'one'}))
