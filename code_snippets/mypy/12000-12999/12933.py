class SupportsStr(Protocol):
    def __str__(self) -> str:
        ...
