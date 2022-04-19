# main.py
from drf_spectacular.utils import Direction


def go(direction: Direction) -> int:
    if direction == "request":
        return 1
    elif direction == "response":
        return 2
