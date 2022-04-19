from typing import TypeVar, Generic, Union

AnyStr = TypeVar('AnyStr', str, bytes)

class PathLike(Generic[AnyStr]):
    def __fspath__(self) -> AnyStr: ...

def readlink(s: Union[AnyStr, PathLike[AnyStr]]) -> AnyStr:
    ...

class BP(PathLike[bytes]):
    def __fspath__(self) -> bytes:
        return b''

class SP(PathLike[str]):
    def __fspath__(self) -> str:
        return ''

reveal_type(readlink(''))
reveal_type(readlink(b''))
reveal_type(readlink(BP()))  # E: Argument 1 to "readlink" has incompatible type "BP"; expected "Union[str, PathLike[str]]"
reveal_type(readlink(SP()))
