from __future__ import annotations

from typing import Callable, Generic, Iterable, Iterator, Optional, Protocol, TypeVar, runtime_checkable

TValue = TypeVar('TValue')


@runtime_checkable
class PNode(Protocol):
    parent: Optional[PNode]
    def parents(self) -> Iterator[PNode]: ...


class Node(Generic[TValue]):
    parent: Optional[Node[TValue]]
    value: TValue

    def __init__(self, value: TValue, parent: Optional[Node[TValue]] = None) -> None:
        self.value = value
        self.parent = parent
        if isinstance(value, PNode):
            value.parent = self

    def parents(self) -> Iterator[Node[TValue]]:
        node = self
        while node is not None:
            yield node
            node = node.parent  # type: ignore


def mypy_test_node(node: PNode) -> None:
    print('node  ', isinstance(node, PNode))


final = Node(0)
node = Node(Node(final))
mypy_test_node(node)
mypy_test_node(final)
print(list(final.parents()))
