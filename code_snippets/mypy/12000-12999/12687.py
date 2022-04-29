from typing import Generic, TypeVar

T = TypeVar("T")


class Animal(Generic[T]):
    pass


class Pooh(Animal[T]):
    pass


class Tigger(Animal[T]):
    pass


def build_friend(animal_type: str) -> Animal[T]:
    friend_map = {constructor.__name__: constructor for constructor in (Pooh, Tigger)}
    return friend_map[animal_type]()     
    # error: Incompatible return value type (got "object", expected "Animal[T]")  [return-value]
