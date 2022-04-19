from typing import Callable, NoReturn, TypeVar


def no_return() -> NoReturn:
    pass


def use_decorated_before_defined() -> int:
    decorated()
    if bool():
        return 0
    else:
        no_return()


T = TypeVar('T')


def wrapper(function: T) -> T:
    return function


def decorator() -> Callable[[T], T]:
    return wrapper


@decorator()
def decorated() -> None: pass


def use_decorated_after_defined() -> int:
    decorated()
    if bool():
        return 0
    else:
        no_return()


def use_wrapped_before_defined() -> int:
    wrapped()
    if bool():
        return 0
    else:
        no_return()


@wrapper
def wrapped() -> None: pass
