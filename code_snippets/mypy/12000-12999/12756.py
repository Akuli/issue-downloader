class AbstractEventLoop:
    # Can't use a union, see mypy issue  # 1873.
    @overload
    @abstractmethod
    def run_until_complete(self, future: Generator[Any, None, _T]) -> _T: ...
    @overload
    @abstractmethod
    def run_until_complete(self, future: Awaitable[_T]) -> _T: ...

import asyncio
import contextvars

async def work() -> None:
    await asyncio.sleep(1)

ctx = contextvars.Context()
loop = asyncio.new_event_loop()
ctx.run(loop.run_until_complete, work())
loop.close()

class AbstractEventLoop:
    # Can't use a union, see mypy issue  # 1873.
    @overload
    @abstractmethod
    def run_until_complete(self, future: Awaitable[_T]) -> _T: ...
    @overload
    @abstractmethod
    def run_until_complete(self, future: Generator[Any, None, _T]) -> _T: ...
