class A:
    @property
    def foo(self) -> int:
        ...
        
    @property  # no error
    def foo(self, value: int) -> int:
        ...


a = A()
