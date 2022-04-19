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

['Array', 'Item', 'MutableSequence', 'Sequence', 'Reversible', 'Collection', 'Sized', 'Iterable', 'Container', 'list', 'object']

[mypy]
pretty = True
show_error_codes = True
show_error_context = True
show_traceback = True
ignore_missing_imports = True
warn_redundant_casts = True
warn_unused_ignores = True

