Foo = int | str

foo: object

isinstance(foo, Foo) # error
isinstance(foo, int | str) # no error
