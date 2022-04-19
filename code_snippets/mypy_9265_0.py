from typing import Any, Callable, TypeVar

_FirstDecoratee = TypeVar("_FirstDecoratee", bound=Callable[..., Any])
_SecondDecoratee = TypeVar("_SecondDecoratee", bound=Callable[..., Any])


def basic_decorator(decoratee: _FirstDecoratee) -> _FirstDecoratee:
    "decorate a function"
    return decoratee


def decorator_transformer(
    decorator: Callable[[_SecondDecoratee], _SecondDecoratee]
) -> Callable[[_SecondDecoratee], _SecondDecoratee]:
    "take a decorator and return a version of it with the same signature"
    def modified_decorator(decoratee: _SecondDecoratee) -> _SecondDecoratee:
        return decoratee
    return modified_decorator


@basic_decorator
def unstacked() -> None:
    "no decorator stack: no error"


@decorator_transformer(basic_decorator)
def stacked() -> None:
    "decorator stack: this should be the same, but it's an error"
