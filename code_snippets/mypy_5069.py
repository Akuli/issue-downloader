from typing import NamedTuple


class A(NamedTuple):
    '''
    value class combining origin coordinate with list of destination coordinates
    '''
    a: str


def foo() -> None:
    A("david")
    greet = lambda a: A("hi " + a)
    greet('moshe')
