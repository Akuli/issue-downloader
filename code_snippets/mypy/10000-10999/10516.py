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

...
fut = loop.run_in_executor(None, g)
x = await fut
return x

[mypy]
disallow_any_decorated = True
disallow_incomplete_defs = True
disallow_untyped_calls = True
disallow_untyped_defs = True
ignore_missing_imports = True
strict_equality = True
warn_unreachable = True
warn_unused_configs = True
warn_unused_ignores = True