from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hashlib import _Hash


def f(h: "_Hash") -> None:
    ...

