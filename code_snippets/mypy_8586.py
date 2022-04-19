from typing import Sequence, Union

def baz(idx: int, arg: Union[int, str]) -> None:
    pass

def foo(the_list: Union[Sequence[int], Sequence[str]]) -> None:
    for idx, val in enumerate(the_list):
        reveal_type(idx)
        reveal_type(val)
        baz(idx, val)
