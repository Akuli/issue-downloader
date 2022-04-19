# example.py
from typing import TypedDict, Literal, Union

# TypedDict interfaces with distinct tag fields.
A = TypedDict('A', {'@type': Literal['type-a'], 'value': str})
B = TypedDict('B', {'@type': Literal['type-b'], 'value': str})

# Tagged union of A and B.
C = Union[A, B]

c: C = {
    '@type': 'type-a',
    'value': 'test',
}
