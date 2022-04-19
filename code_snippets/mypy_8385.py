# module: foo.py
def foo() -> None | baz.Baz | tuple[int, int]:
    ...

# module: bar.py
def bar() -> ReturnType[foo.foo]:
    ...
