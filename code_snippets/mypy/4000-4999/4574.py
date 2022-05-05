class Base(object):
    def foo(self):
         # type: () -> None
         a = self.static_foo()

class SubClass(Base):
    static_foo = staticmethod(lambda: 5)
