from typing import Dict, Optional

foo_dict: Dict[str, Optional[str]] = {'bar': 'baz'}

if foo_dict['bar'] is not None:
    foo_dict['bar'] = None
    foo_dict['bar'].upper()

from dataclasses import dataclass
from typing import Optional

@dataclass
class Foo:
    bar: Optional[str]

foo = Foo(bar='baz')

if foo.bar is not None:
    foo.bar = None
    foo.bar.upper()
