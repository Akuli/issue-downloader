from pathlib import Path
import attr
@attr.s
class Options:
    path: Path = attr.ib(default='.', converter=Path)
