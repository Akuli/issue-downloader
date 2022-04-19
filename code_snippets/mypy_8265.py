foo: Union[int, Callable[[Any], int]]
bar: Callable[[Any], int]

foo = lambda _: 0

# case A
# no errors:
if callable(foo):
    bar = foo
else:
    bar = lambda _: foo

# case B
# error: Incompatible return value type (got "Union[int, Callable[[int], int]]", expected "int")
bar = foo if callable(foo) else lambda _: foo
