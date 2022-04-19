class A:
    def foo(self) -> None:
        print()

class B(A):
    def foo(self) -> NoReturn:
        warnings.warn("this is an unsupported operation", DeprecationWarning)
        raise NotImplementedError()


B().foo()  # I would like a warning that this is unsupported
