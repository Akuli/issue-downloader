class Foo:
    pass


class Outer:
    foo_class = Foo

    def foo_method(self):
        class FooInner(self.foo_class):
            pass
