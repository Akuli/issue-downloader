class X:
    def __new__(cls) -> "X":
        return super(type, cls).__new__(cls)    # error: Argument 2 for "super" not an instance of argument 1
