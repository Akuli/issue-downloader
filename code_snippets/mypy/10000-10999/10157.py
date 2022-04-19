@overload
def func1(
    a: str,
    b: Literal[False] = ...,
) -> List[str]: ...
@overload
def func1(
    a: str,
    b: bool = ...,
) -> List[Union[str, int]]: ...

_T = TypeVar("_T")
@overload
def func2(
    a: _T,
    b: Literal[False] = ...,
) -> List[_T]: ...
@overload
def func2(
    a: _T,
    b: bool = ...,
) -> List[Union[_T, int]]: ...
