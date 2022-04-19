import asyncio
from typing import AsyncGenerator


async def get_value(v: int) -> int:
    await asyncio.sleep(1)
    return v + 1


def get_generator() -> AsyncGenerator[int, None]:
    return (await get_value(v) for v in [1, 2, 3])


async def test() -> None:
    print(type(get_generator()))
    async for x in get_generator():
        print(x)


asyncio.get_event_loop().run_until_complete(test())
