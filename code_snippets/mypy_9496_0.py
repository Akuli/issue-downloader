from typing import Callable, TypeVar

Fn = TypeVar("Fn", bound=Callable[..., object])
