foo: list[str]
if isinstance(foo, list):
    reveal_type(foo) # note: Revealed type is "list[str]"
else:
    # error: Unused "type: ignore" comment
    # note: Revealed type is "<nothing>"
    reveal_type(foo) #type:ignore[unreachable]
