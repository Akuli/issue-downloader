from typing import TypedDict

def my_function(foo: int, bar: int) -> None:
    pass

class MyTypedDict(TypedDict):
    # foo: int
    bar: int

    
a: MyTypedDict = {'bar': 1}

my_function(**a) # mypy - error: Missing positional argument "bar" in call to "my_function"
my_function(bar=1) # mypy - error: Missing positional argument "foo" in call to "my_function"
