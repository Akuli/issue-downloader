from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import (
    AsyncContextManager,
    AsyncIterator,
    Callable,
    Generic,
    ParamSpec,
    TypeVar,
)

_Input = ParamSpec("_Input")
_Result = TypeVar("_Result")


@dataclass
class Foo(Generic[_Input, _Result]):
    func: Callable[_Input, AsyncContextManager[_Result]]

    @asynccontextmanager
    async def boo(
        self, *args: _Input.args, **kwargs: _Input.kwargs
    ) -> AsyncIterator[_Result]:
        async with self.func(*args, **kwargs) as fr:
            yield fr
