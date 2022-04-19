class BoundedMeta(type):
    def __getitem__(self, args):
        ...

class Bounded(metaclass=BoundedMeta):
    ...

Age = Bounded[int, 0:150]

class Person:
    age: Age
