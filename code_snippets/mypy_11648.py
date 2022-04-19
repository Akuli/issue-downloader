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

class A: ...
class B: ...
C = A | B
reveal_type(C) # Revealed type is "builtins.object"
isinstance(object(), C) # error: Parameterized generics cannot be used with class or instance checks
                        # error: Argument 2 to "isinstance" has incompatible type "object"; expected "Union[type, UnionType, Tuple[Union[type, UnionType, Tuple[Any, ...]], ...]]"

isinstance(object(), int | list[int]) # no error (should be "error: Parameterized generics cannot be used with class or instance checks")

