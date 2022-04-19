from __future__ import annotations

import asyncio
import typing as t
from contextlib import asynccontextmanager

import typing_extensions as te


class LockProto(te.Protocol):
    async def with_lock(self) -> t.AsyncContextManager[str]: ...


class Consumer:
    def __init__(self, locker: LockProto) -> None:
        self.locker = locker

    def run(self) -> None:
        async with self.locker.with_lock() as name:
            print(name)


class SockLock:
    @asynccontextmanager
    async def with_lock(self) -> t.AsyncGenerator[str, None]:
        yield 'some-string'


async def main() -> None:
    cons = Consumer(SockLock())
    await cons.run()


if __name__ == '__main__':
    asyncio.run(main())
