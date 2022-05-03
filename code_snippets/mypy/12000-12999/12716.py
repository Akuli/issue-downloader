def acquire(func: Callable[Concatenate[Any, str, _P], Awaitable[_T]]) -> Callable[Concatenate[Any, _P], Awaitable[_T]]:
    ...

@overload
async def get(self, key: bytes, default: None = ...) -> Union[bytes, _T, None]:
    ...
@overload
async def get(self, key: bytes, default: _U) -> Union[bytes, _T, _U]:
    ...
@acquire
async def get(
    self, conn: str, key: bytes, default: Optional[_U] = None
) -> Union[bytes, _T, _U, None]:
    ...

get(b"foo")
