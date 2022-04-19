from typing import TypedDict

class FooDict(TypedDict):
    foo: int
    bar: int
    
foo = FooDict(foo=3, bar=3)

print(foo["foo"]) # Works
print(foo["bar"]) # Works
reveal_type(("foo", "bar")) # Revealed type is 'Tuple[Literal['foo']?, Literal['bar']?]'

for key in ("foo", "bar"):
    reveal_type(key) # Revealed type is 'builtins.str'
    print(foo[key]) # TypedDict key must be a string literal; expected one of ('foo', 'bar')
