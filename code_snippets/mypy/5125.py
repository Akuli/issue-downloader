from typing import Any, Callable, Awaitable

AnyFunction = Callable[..., Awaitable[Any]]

def retry() -> Callable[[AnyFunction], AnyFunction]:
    def decorator(fn: AnyFunction) -> AnyFunction:
        return fn
    return decorator

class B:
    async def run(self) -> bool:
        return True

class C(B):
    @retry()
    async def run(self) -> bool:
        return True
