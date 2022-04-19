from dataclasses import dataclass


@dataclass
class Foo:
    value: int


foo = Foo(1) # no error


class Bar:
    value: int


Baz = dataclass(Bar)

baz = Baz(1) # Too many arguments for "Bar"  [call-arg]
