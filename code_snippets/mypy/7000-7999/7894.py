class Foo:
  num: int = 1
  msg: str = "hello"

FooProtocol = protocol(Foo, include_private=False)

FooLookalike = NamedTuple("FooLookalike", [("num", int), ("msg", str)])

# ok
maybe_foo: FooProtocol = FooLookalike(num=2, msg="bye")

# ok
maybe_foo = Foo()

# safely cast when using Fakes in a test
test_foo(cast(Foo, maybe_foo))

