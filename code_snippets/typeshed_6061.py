# repro.py
import typing
from io import TextIOWrapper, BufferedIOBase

def badfunc(stream: BufferedIOBase) -> TextIOWrapper:
    return TextIOWrapper(stream)

def goodfunc(stream: typing.IO[bytes]) -> TextIOWrapper:
    return TextIOWrapper(stream)
