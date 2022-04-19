from typing import Generic, TypeVar


T_contra = TypeVar('T_contra', contravariant=True)


class Animal:
    pass


class Cat(Animal):
    pass


class AnimalBox(Generic[T_contra]):
    def __init__(self, animal: T_contra):
        pass


def print_box(a: AnimalBox[Cat]):
    pass


animal = Animal()

print_box(AnimalBox(animal))  # error: Argument 1 to "AnimalBox" has incompatible type "Animal"; expected "Cat"

box = AnimalBox(animal)
print_box(box)  # OK
