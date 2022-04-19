
foo: int = 1
Foo = type[foo]  # equivalent to Foo = int

def bar(x: string) -> None :
    ...
Bar = type[bar]  # equivalent to Bar = Callable[[str], None]
