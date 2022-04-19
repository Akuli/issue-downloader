from typing_extensions import Final, Literal

s: Final[Literal['ccc']] = 'ccc'
s1: Literal[s] = s
