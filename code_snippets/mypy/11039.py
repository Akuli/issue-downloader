import enum

class MyEnumMeta(enum.EnumMeta):
  def __getitem__(self, indexOrSlice):
    if isinstance(indexOrSlice, (int, slice)):
      return list(self)[indexOrSlice]
    else:
      return enum.EnumMeta.__getitem__(self, indexOrSlice)

class MyEnum(enum.Enum, metaclass=MyEnumMeta): pass

class Period(MyEnum):
  A = "a"
  B = "b"
  C = "c"

print(Period["A"])
print(Period[1])    # type: ignore[misc]
print(Period[:2])   # type: ignore[misc]
