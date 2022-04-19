from typing import List, Tuple, Union


Nested = Union[
    List[str],
    List[List[str]]
]

FlatWithCoordinates = Union[
    List[Tuple[str, int]],
    List[Tuple[str, int, int]],
]


def f(a: Nested) -> FlatWithCoordinates:

    if not isinstance(a[0], List):
        return [
            (s, x)
            for x, s in enumerate(a)
        ]
    else:
        return [
            (s, x, y)
            for x, ss in enumerate(a)
            for y, s in enumerate(ss)
        ]


# test

assert f(['a', 'b', 'c']) == [('a', 0), ('b', 1), ('c', 2)]
assert f([['a', 'b', 'c'], ['x', 'y', 'z']]) == [
    ('a', 0, 0),
    ('b', 0, 1),
    ('c', 0, 2),
    ('x', 1, 0),
    ('y', 1, 1),
    ('z', 1, 2)
]
