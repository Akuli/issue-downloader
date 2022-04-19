from typing_extensions import Protocol


class Func(Protocol):
    def __call__(self, __a: int, **kwargs: str) -> None:
        #              ^^^ positional-only arg
        ...
    # Same error when using PEP 570 positional-only syntax:
    # def __call__(self, a: int, /, **kwargs: str) -> None:


def myfunc(a: int, **kwargs: str) -> None:
    pass


f: Func = myfunc
