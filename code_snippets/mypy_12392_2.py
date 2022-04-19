B = Type[int] | str  # error: Unsupported left operand type for | ("object")
D: TypeAlias = Type[int] | str  # error: Unsupported left operand type for | ("object")
G = str | Type[int]  # no error
