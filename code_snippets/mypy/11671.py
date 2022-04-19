class FooMetaclass(type):
    pass
class Foo(metaclass=FooMetaclass):
    pass

fm: FooMetaclass
reveal_type(fm)  # note: Revealed type is "__main__.FooMetaclass"
if issubclass(fm, Foo):
    reveal_type(fm)  # note: Revealed type is "__main__.FooMetaclass"
