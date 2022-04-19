# mypy: enable-error-code truthy-bool

class Foo:
    pass
foo = Foo()
# Error: "foo" has type "Foo" which does not implement __bool__ or __len__ so it could always be true in boolean context
if foo:
    ...
