from collections import deque
from typing import TypedDict, Dict, Deque


class MyTypedDict(TypedDict):
    pass


Step = Dict[int, MyTypedDict]


a: Deque[Step] = deque([{}])   # OK
b: Deque[Step] = deque(({},))  # MyPy error
