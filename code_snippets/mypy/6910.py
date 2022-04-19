from dataclasses import dataclass, fields


@dataclass
class Foo:
    value: str


fields(Foo)[0].default_factory
