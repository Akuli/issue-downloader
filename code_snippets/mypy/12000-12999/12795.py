import typing


class P(typing.Protocol):
    __name__: str

    def __call__(self) -> None:
        return


def DEFAULT_P() -> None: ...


def f(o: P) -> None:
    o()
    o.__name__

f(DEFAULT_P)
