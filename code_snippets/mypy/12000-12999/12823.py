from typing import Optional


class Cat:
    pass


class Dog:
    pass


class MyClass:
    def __init__(self) -> None:
        self.pet: Optional[Dog | Cat] = None

    def get_pet(self) -> Optional[Dog | Cat]:
        if input() == 'yes':
            self.pet = Cat()
        else:
            self.pet = Dog()
        return self.pet  # (incorrect Mypy error on this line!)
