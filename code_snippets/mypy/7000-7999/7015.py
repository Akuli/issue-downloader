from typing_extensions import final


class Base:
    @final
    def __init__(self):
        pass


class A(Base):
    def __init__(self):  # no error raised
        pass


class B(Base):
    def __init__(self) -> None:  # raises an error
        pass
