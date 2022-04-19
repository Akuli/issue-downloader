class MyEnum(str, enum.Enum):
    value: str
    FIRST = 'first'

class MyEnum(enum.Enum[str]):
    FIRST = 'first'

