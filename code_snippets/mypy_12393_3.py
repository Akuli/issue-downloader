X = int | Callable[[], str | bool]  # error: Unsupported left operand type for | ("Type[str]")
Y = int | Callable[[str | bool], str]  # error: Unsupported left operand type for | ("Type[str]")
