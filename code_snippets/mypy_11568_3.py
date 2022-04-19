from typing import Literal

Direction = Literal['request', 'response']


def go(direction: Direction) -> int:
    if direction == "request":
        return 1
    elif direction == "response":
        return 2
