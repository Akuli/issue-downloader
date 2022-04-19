import functools

class Foo:
    bar = functools

foo = Foo()
foo.bar  # error: Member "bar" is not assignable
