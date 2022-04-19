decorator: int = 3

@decorator  # no error
class A:
    pass

class B:
    pass
NewB = decorator(B)  # E: "int" not callable
