class A:
    def __init__(self, x: int) -> None:
        self.__x = x  # replace this with pass and mypy reports the error


class B(A):
    def __init__(self) -> None:
        A.__init__(self, self.__x)


B()
