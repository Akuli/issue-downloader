
if isinstance(foo_union, SupportsFunc):
    reveal_type(foo_union)  # N: Revealed type is '__main__.FooOverload'
else:
    reveal_type(foo_union)  # N: Revealed type is '__main__.Foo'

