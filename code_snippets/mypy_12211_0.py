_ResponseType = TypeVar("_ResponseType")


SyncFunc: TypeAlias = Callable[..., _ResponseType]
Coro: TypeAlias = Callable[..., Coroutine[Any, Any, _ResponseType]]

SyncFuncOrCoro: TypeAlias = Coro[_ResponseType] | SyncFunc[_ResponseType]

