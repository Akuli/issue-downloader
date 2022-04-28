# filter-mypy.py
path_parts: List[Optional[str]] = ["foo", None, "bar"]

"/".join(filter(None, path_parts))
"/".join(filter(bool, path_parts))
"/".join(filter(lambda s: isinstance(s, str), path_parts))

class filter(Iterator[_T], Generic[_T]):
    @overload
    def __init__(self, __function: None, __iterable: Iterable[_T | None]) -> None: ...
    @overload
    def __init__(self, __function: Callable[[_S], TypeGuard[_T]], __iterable: Iterable[_S]) -> None: ...
    @overload
    def __init__(self, __function: Callable[[_T], Any], __iterable: Iterable[_T]) -> None: ...
