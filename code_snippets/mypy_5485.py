from dataclasses import dataclass
from typing import Callable

@dataclass
class Repro:
    fn: Callable[[int], str]

r = Repro(fn=repr)
assert "1" == r.fn(1)

class Repro:
    def __init__(self, fn: Callable[[int], str]) -> None:
        self.fn = fn

[mypy]
warn_redundant_casts = True
warn_unused_ignores = True
incremental = True

follow_imports = normal
ignore_missing_imports = True
disallow_untyped_calls = True
disallow_untyped_defs = True
check_untyped_defs = True
warn_return_any = True
warn_no_return = True
no_implicit_optional = True
strict_optional = True
