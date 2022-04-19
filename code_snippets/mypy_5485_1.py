class Repro:
    def __init__(self, fn: Callable[[int], str]) -> None:
        self.fn = fn
