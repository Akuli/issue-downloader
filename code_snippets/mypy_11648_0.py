from typing import Union

class MyUnion(type): ...

class Meta(type):
    
    def __or__(self, other) -> MyUnion: ... # type: ignore
    
class Foo(metaclass=Meta): ...

reveal_type(Foo | Foo) # line 12
isinstance(object(), Foo | Foo)
Bar = Foo | Foo
reveal_type(Bar) # line 14
isinstance(object(), Bar) # line 15
