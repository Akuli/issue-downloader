@enum.unique
class MyEnumClass(Enum, metaclass=MyEnumMetaClass):
    OUT_OF_STOCK = "Out of Stock"
    LOW_STOCK = "Low Stock"
    IN_STOCK = "In Stock"
    EXCESS = "Excess"
