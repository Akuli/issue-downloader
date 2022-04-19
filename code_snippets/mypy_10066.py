class B1:
    def foo(self) -> int:
        ...

class B2:
    def foo(self) -> str:
        ...

class Composite(B1, B2):  # type: ignore
    ...

class AppClass1(Composite):  # <-- no error here
    ...

class AppClass2(Composite, object):  # <-- error here!
    ...
