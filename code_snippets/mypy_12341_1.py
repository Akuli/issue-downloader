def foo(bar:int) -> str: ...
def baz() -> int: ...

a = ( # type: ignore[call-arg]
    "something" 
    if baz() > 0 else 
    foo() # ignore currently needs to be here
)  # formatters (eg. black) often put ignore here
