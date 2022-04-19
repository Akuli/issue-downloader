from typing import TypeVar, Generic, List

ContainedType = TypeVar('ContainedType', bound='ContainedCls')
SubContained = TypeVar('SubContained')
T = TypeVar('T')

class Root_wrong(Generic[ContainedType[SubContained]]):
    def __init__(self, ct):
        # type: (ContainedType[SubContained]) -> None
        self.contained = ct

    def iter_subcontained(self):
        # type: () -> List[SubContained]
        return self.contained.items

class ContainedCls(Generic[T]):
    def __init__(self, items):
        # type: (List[T]) -> None
        self.items = items
