class list:
    def __add__(self, x: List[_T]) -> List[_T]: ...
    def __iadd__(self: _S, x: Iterable[_T]) -> _S: ...

class list:
    def __add__(self, x: List[_S]) -> List[Union[_T, _S]]: ...
    # __iadd__ unchanged
