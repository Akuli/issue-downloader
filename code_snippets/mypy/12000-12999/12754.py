from typing import TypedDict

def my_function(foo: int, bar: int, baz: str) -> None:
    pass

class MyTypedDict(TypedDict, total=False):
    foo: int
    bar: int
    baz: str
    
    
a: MyTypedDict = {'bar': 1}

my_function(**a) # Should be error here, as a doesn't contain foo or baz
