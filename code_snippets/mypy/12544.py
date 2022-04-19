from dataclasses import dataclass
from typing import TypeAlias

class Foo:
    x = 1

@dataclass
class A:
    ShortName: TypeAlias = Foo
    var: int = ShortName.x
