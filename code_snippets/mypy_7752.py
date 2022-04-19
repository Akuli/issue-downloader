from typing_extensions import Literal, TypedDict

class TDict(TypedDict):
    KEY1: int
    KEY2: int

d1: TDict = {'KEY1': 1, 'KEY2': 2}

key2: Literal['KEY1']
d2: TDict = {key2: 1, 'KEY2': 2}

key3: Literal['KEY1', 'KEY2']
d3: TDict = {key3: 1, 'KEY2': 2}  # error: Expected TypedDict key to be string literal
