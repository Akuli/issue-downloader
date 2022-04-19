from typing import AnyStr
from typing_extensions import Protocol
class PathLike(Protocol[AnyStr]):
    def __fspath__(self) -> AnyStr: ...
