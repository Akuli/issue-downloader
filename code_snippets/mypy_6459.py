class Foo():
    var = 1 

class Bar(Foo):
    def __init__(self, x): 
        pass

(cls.var for cls in (Foo, Bar))
