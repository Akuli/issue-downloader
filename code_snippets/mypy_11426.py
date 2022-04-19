from __future__ import annotations

from typing import Literal

Foo = Literal[1, 2]

Bar = Foo | Literal[3] # error: Unsupported left operand type for | ("object")
