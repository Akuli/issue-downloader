import typing

def round_it(x: typing.SupportsRound[int]) -> int:
    return round(x)

round_it(3.2)

@overload
def __round__(self, ndigits: None = ...) -> int: ...
