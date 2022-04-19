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
