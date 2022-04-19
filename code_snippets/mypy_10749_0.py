class X:
    def __init__(self, value: str | None = None, parent: X | None = None) -> None:
        if value is None:
            if parent is not None and parent.value is not None:
                value = "something"
            else:
                value = "something_else"
        reveal_type(value)
        self.value = value
