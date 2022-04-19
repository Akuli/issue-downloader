from typing import Literal


def f(x: Literal["a", "b"]):
    ...


def g(x: str):
    if x == "a":
        ...
    elif x == "b":
        ...
    else:
        raise ValueError()
    f(x) # ERROR: "f" has incompatible type "str"; expected "Union[Literal['a'], Literal['b']]"
