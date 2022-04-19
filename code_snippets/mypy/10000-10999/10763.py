from typing import *

import asyncio

class Readable(Protocol):
    def read(self) -> bytes:
        pass
    
class Seekable(Readable, Protocol):
    def seek(self, v: int) -> int:
        pass
    
T_readable = TypeVar("T_readable", bound=Readable)
T_seekable = TypeVar("T_seekable", bound=Seekable)


class AsyncFile(Generic[T_readable]):
    def __init__(self, v: T_readable):
        self._v = v
        
    async def seek(self: AsyncFile[T_seekable], v: int) -> int:
        return await asyncio.to_thread(self._v.seek, v)
        
    async def read(self) -> bytes:
        return await asyncio.to_thread(self._v.read)
        
        
class Foo:
    def read(self) -> bytes:
        return b"foo"
        
async def amain() -> None:
    af = AsyncFile(Foo())
    reveal_type(AsyncFile)  # note: Revealed type is "def [T_readable <: main.Readable] (v: T_readable`1) -> main.AsyncFile[T_readable`1]"
    await af.read()
    await af.seek(0)
