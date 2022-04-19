x = "foo" # type: Optional[str]
x + "bar"  # E: Unsupported operand types for + ("Union[str, None]" and "str")
