from typing import overload, Callable

@overload
def sub(pattern: str, repl: Callable[[str], str]) -> str: ...
@overload
def sub(pattern: bytes, repl: Callable[[bytes], bytes]) -> bytes: ...
def sub(pattern: object, repl: object) -> object:
    raise NotImplementedError

def better_snakecase(text: str) -> str:
    text = sub(r"([A-Z])([A-Z]+)([A-Z](?:[^A-Z]|$))", lambda match: f"{match}")
    return text
