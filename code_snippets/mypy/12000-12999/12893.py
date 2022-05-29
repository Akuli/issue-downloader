class A:
    def __init__(*, self) -> None:
        ...


a = A() # runtime error - TypeError: A.__init__() takes 0 positional arguments but 1 was given
