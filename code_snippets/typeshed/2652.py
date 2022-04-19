import asyncio
from typing import List

async def five() -> int:
    return 5

async def runner() -> List[int]:
    fives = await asyncio.gather(five(), five(), five())
    print(type(fives))  # prints `<class 'list'>`
    print(fives)  # prints `[5, 5, 5]`
    return fives

loop = asyncio.get_event_loop()
result: List[int] = loop.run_until_complete(runner())
