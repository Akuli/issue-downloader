import typing

class Base:
    A: typing.Type[Base]

class One(Base):
    class A(Base):  # overrides Base.A
        pass

class Two(Base):
    class A(One):  # overrides Base.A
        pass


T = typing.TypeVar('T', bound=Base)

class Foo(typing.Generic[T]):                 # the generic
    def foo(self, a: typing.Type[T.A]) -> T:  # <-- here, see T.A
        ...

f: Foo[Two] = Foo()
f.foo(Two.A)        # line 22 is here
