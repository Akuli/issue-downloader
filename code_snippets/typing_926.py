R_T = TypeVar("R_T")
P = ParamSpec("P")

async def maybe_coroutine(func: Callable[P, Union[R_T, Coroutine[Any, Any, R_T]]], *args: P.args, **kwargs: P.kwargs) -> R_T:
    value = func(*args, **kwargs)

    if isawaitable(value):
        value = await value

    return value
