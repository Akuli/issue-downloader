from typing import Generic, TypeVar, NamedTuple


T = TypeVar('T')


class Node(Generic[T]):
    v: T


class IntegerNode(Node[int], NamedTuple('IntegerNode', [('v', int)])):
    pass
