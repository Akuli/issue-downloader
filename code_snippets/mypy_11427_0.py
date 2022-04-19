from typing import Optional
from collections.abc import MutableSequence


class Item:
    def __init__(self, comment: Optional[str] = None):
        self._comment = comment


class Array(Item, MutableSequence, list):
    def __init__(self, values: list, comment: Optional[str] = None):
        Item.__init__(self, comment)
        list.__init__(self, values)


if __name__ == '__main__':
    a = Array([0, 1, 2])
    print([p.__name__ for p in a.__class__.__mro__])
