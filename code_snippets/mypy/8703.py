from typing import List, Union
from dataclasses import dataclass, field


def foo():
    @dataclass
    class Foo:
        foo: int

        def __call__(self) -> asdf:
            ...
