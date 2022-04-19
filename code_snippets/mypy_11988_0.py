class A(TypedDict):
    a: str

class BC(TypedDict, total=False):
    other: str
    a: str

Spec = Union[A, BC]

class Config(TypedDict):
    prop: Spec
