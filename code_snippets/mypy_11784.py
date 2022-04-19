from __future__ import annotations

import enum


class E(enum.Enum):
    A = (1,)
    B = (2,)

    @property
    def x(self) -> E:
        reveal_type(type(self).__iter__)
        reveal_type(iter(type(self)))
        reveal_type(tuple(type(self)))
        vals = tuple(type(self))
        return vals[(vals.index(self) + 1) % len(vals)]


reveal_type(iter(E))
