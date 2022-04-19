import asyncio

from typing import Optional


def g() -> int:
    return 1


async def f(x: Optional[int] = None) -> int:
    loop = asyncio.get_running_loop()

    if x is not None:
        return x
    x = await loop.run_in_executor(None, g)
    return x
