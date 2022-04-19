from typing import TypeAlias, Union


class Dog:
    pass

class Cat:
    pass

class Salmon:
    pass

class Trout:
    pass


Mammal: TypeAlias = Dog | Cat

Fish: TypeAlias = Salmon | Trout

Animal: TypeAlias = Mammal | Fish  # type error!!

Animal2: TypeAlias = Union[Mammal, Fish]  # no type error, as expected
