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
