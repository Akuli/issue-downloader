from enum import Enum

class Foo(Enum):
    ""

Bar: type = Enum('Bar', ['X', 'Y']) # line 6
Baz: type = Foo('Baz', ['X', 'Y']) # line 7

bar: Bar = Bar.X # line 9
baz: Baz = Baz.Y # line 10
