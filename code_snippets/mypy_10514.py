from typing import Literal, Union

Foo = Union[Literal[-1], Literal[42]]


def correct(f: Foo) -> None:
    if f == 42:
        reveal_type(f)  # Revealed type is 'Literal[42]'
    else:
        reveal_type(f)  # Revealed type is 'Literal[-1]'


def also_correct(f: Foo) -> None:
    if f == -2:
        reveal_type(f)  # Non-overlapping equality check (left operand type: "Union[Literal[-1], Literal[42]]", right operand type: "Literal[-2]")
    else:
        reveal_type(f)  # Revealed type is 'Union[Literal[-1], Literal[42]]'


def wrong(f: Foo) -> None:
    if f == -1:
        reveal_type(f)  # Revealed type is '<nothing>'
    else:
        reveal_type(f)  # Revealed type is 'Union[Literal[-1], Literal[42]]'
