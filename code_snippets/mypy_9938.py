from typing import Dict


class MyObject(str):
    """
    >>> tuple(MyObject('G'))
    ('G', 71)
    """
    def __iter__(self):
        return iter((self, ord(self)))


def get_mapping() -> Dict[str, int]:
    """
    >>> get_mapping()
    {'a': 97, 'b': 98}
    """
    items = MyObject('a'), MyObject('b')
    return dict(items)
