from mypy_extensions import TypedDict


class Grandparent(TypedDict):
    a: str


class ParentB(Grandparent):
    b: str


class ParentC(Grandparent):
    c: str


class Child(ParentB, ParentC):
    pass
