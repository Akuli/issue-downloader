Foo = Literal["foo"]
Bar = NewType("Bar", str)

Baz = NewType("Baz", Foo)
