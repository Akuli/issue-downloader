from dataclasses import dataclass
from typing import Any, Callable

# here `Parent` is a frozen dataclass, but `Child` is not

@dataclass(frozen=True)
class Parent:
    __call__: Callable[..., None]

    def __call__(self, *args: Any, **kwargs: Any) -> None:  # type: ignore
        raise NotImplementedError


class Child(Parent):
    def __call__(self, value: int) -> None:
        ...
