class Foo(TypedDict):
    a: int
    b: int


class Bar(Foo):
    c: int


foo = Foo(a=1, b=2)
