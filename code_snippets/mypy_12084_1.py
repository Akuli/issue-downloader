from typing import Any, Callable

# here both `Parent` and `Child` are "regular" classes

class Parent:
    __call__: Callable[..., None]

    def __call__(self, *args: Any, **kwargs: Any) -> None:  # type: ignore
        raise NotImplementedError


class Child(Parent):
    def __call__(self, value: int) -> None:
        ...
