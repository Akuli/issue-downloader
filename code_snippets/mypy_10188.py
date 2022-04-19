from typing import Generator

def f() -> Generator[int, None, str]:
    yield 1
    return "lol"

def g() -> Generator[int, None, None]:
    x = [(yield from f()) for lel in range(5)]
    print(x)        # <generator object g.<locals>.<listcomp> at 0x7fba92696a20>
    reveal_type(x)  # List[str]

g()
