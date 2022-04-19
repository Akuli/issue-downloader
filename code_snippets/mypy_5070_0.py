from typing import AsyncGenerator

async def gen1() -> AsyncGenerator[str, None]:
    pass
reveal_type(gen1)

async def gen2() -> AsyncGenerator[str, None]:
    yield 'tick'
reveal_type(gen2)
