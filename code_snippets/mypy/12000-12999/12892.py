class A:
    @property
    def foo(self) -> int:
        ...
    @foo.setter
    def foo(self, value: int, value2: str) -> None: # no mypy error
        ...


a = A()

a.foo = 1 # runtime error - TypeError: A.foo() missing 1 required positional argument: 'value2'
