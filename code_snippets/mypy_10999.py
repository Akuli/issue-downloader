from typing import List, Union, Generic, TypeVar

T = TypeVar("T")


class Tree(Generic[T]):
    children: "List[Union[T, Tree[T]]]"

    def __init__(self, children: "List[Union[T, Tree[T]]]") -> None:
        self.children = children

    def all_sub_trees(self) -> None:
        sub_trees: "List[Tree[T]]" = [self]
        reveal_type(sub_trees)
        only_child_trees = [v for v in self.children if isinstance(v, Tree)]
        reveal_type(only_child_trees)
        # 3 equivalent statements (ignoring that the first mutates instead of replacing)
        sub_trees.extend(only_child_trees)
        sub_trees = sub_trees + only_child_trees
        sub_trees += only_child_trees
