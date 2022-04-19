from typing import Dict
from dataclasses import dataclass


@dataclass
class Foo:
    bar: bool


@dataclass
class Bar:
    baz: bool


foo_registry: Dict[str, Foo] = {}
bar_registry: Dict[str, Bar] = {}

use_foo = True

registry = foo_registry if use_foo else bar_registry
registry.get('asdfsdf')
