class A:
    @property
    def f(self) -> int: ...
a = A()
del a.f  # no mypy error; runtime AttributeError
