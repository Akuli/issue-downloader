from enum import Enum
class EnumClass(Enum):
    one = 1

EnumAlias = EnumClass
EnumAlias['one']
