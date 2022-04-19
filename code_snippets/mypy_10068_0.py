Type = type

class MyInt(int):
    pass

x_type: Type[int] = MyInt
