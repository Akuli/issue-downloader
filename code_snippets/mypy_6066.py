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

class Root(Generic[ContainedType]):
    def __init__(self, ct):
        # type: (ContainedType) -> None
        # I know because of the bound that ContainedType will have a parameter of its own, but I
        # can't refer to it in the `class Root` declaration because TypeVars can't be indexed.
        # and the index to Generic has to be a typevar
        self.contained = ct

    def iter_subcontained(self):
        # what goes here?
        return self.contained.items


reveal_type(Root(ContainedCls([1])).iter_subcontained())  # Any

class Root2(Generic[ContainedType, SubContained]):
    def __init__(self, ct):
        # type: (ContainedType) -> None
        # I know because of the bound that ContainedType will have a parameter of its own, but I
        # can't refer to it in the `class Root` declaration because TypeVars can't be indexed.
        # and the index to Generic has to be a typevar
        self.contained = ct

    def iter_subcontained(self):
        # type: () -> List[SubContained]
        return self.contained.items


reveal_type(Root2(ContainedCls([1])).iter_subcontained())  # builtins.list[<nothing>]

# not matching is not an error
reveal_type(Root2[ContainedType[int], str](ContainedCls([1])).iter_subcontained())  # builtins.list[str]

class Root3(Generic[T]):
    def __init__(self, ct1, ct2):
        # type: (ContainedCls[T], ContainedCls[T]) -> None
        self.contained = ct1
        self.contained2 = ct2

    def iter_subcontained(self):
        # type: () -> List[T]
        return self.contained.items


class ContainedClsPrime(ContainedCls):
    pass


# no way to ensure that ct1 and ct2 are the same container type
# in fact, they aren't even constrained to have the same T!
x = Root3[int](ContainedCls([1]), ContainedClsPrime(['definitely not an int']))
reveal_type(x.iter_subcontained())  # builtins.list[str]
reveal_type(x.contained2.items[0])  # builtins.int* !!!
