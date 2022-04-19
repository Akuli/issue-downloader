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
