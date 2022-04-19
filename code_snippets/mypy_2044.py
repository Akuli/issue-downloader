from typing import Generic, TypeVar, Set, List, Iterable

T = TypeVar('T')

class Node:
    def __init__(self, children: List['Node']) -> None:
        self.children = children

    def accept(self, visitor: 'Visitor[T]') -> T:
        pass

class NodeChild(Node):
    def accept(self, visitor: 'Visitor[T]') -> T:
        return visitor.visit_node_child(self)

class Visitor(Generic[T]):
    def visit_node_child(self, node: NodeChild) -> T:
        pass

class ExampleVisitor(Visitor[Set[str]]):
    def _visit(self, nodes: List[Node]) -> Set[str]:
        output = set()  # type: Set[str]
        for node in nodes:
            output.update(node.accept(self))  # Error here
        return output

    def visit_node_child(self, node: NodeChild) -> Set[str]:
        return {'a'} | self._visit(node.children)
