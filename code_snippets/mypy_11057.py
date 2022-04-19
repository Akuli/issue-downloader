class Base:
    def __init_subclass__(cls, keyword: int = 0): ...
    
class Derived(Base, keyword='fail'): ...

class Meta(type): ...

class Base(metaclass=Meta):
    def __init_subclass__(cls, keyword: int = 0): ...
    
class Derived(Base, keyword='fail'): ...
