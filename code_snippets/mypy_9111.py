import asyncio
from typing import NoReturn, Set

tasks: Set[asyncio.Task[NoReturn]] = set()
