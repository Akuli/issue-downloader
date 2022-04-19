from dataclasses import dataclass
from typing import Optional

@dataclass
class Foo:
    bar: Optional[str]

foo = Foo(bar='baz')

if foo.bar is not None:
    foo.bar = None
    foo.bar.upper()
