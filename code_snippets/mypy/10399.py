from typing import Any, Protocol, Union

class HasName(Protocol):
    def __name__(self) -> str:
        ...

class Animal:
    def __name__(self) -> str:
        ...

class Dog(Animal):
    def __name__(self) -> str:
        ...

    def run(self) -> None:
        print("Run Spot Run!")

    def bark(self) -> None:
        print("Ruff!")

class Cat:
    def __name__(self) -> str:
        ...

    def run(self) -> None:
        print("Run Kitty Run!")

    def purr(self) -> None:
        print("Purr!")

class AnimalMember:
    def __get__(self, instance: Any, owner: Any) -> Animal:
        ...

    def __set__(self, instance: Any, value: HasName) -> None:
        ...

class Struct:
    member = AnimalMember()

def test_descriptor(cat: Cat, dog: Dog, cat_or_dog: Union[Cat, Dog]):
    inst = Struct()

    inst.member = cat_or_dog
    reveal_type(inst.member)  # mypy: Revealed type is 'Animal'
    inst.member.run()  # mypy: "Animal" has no attribute "run"
    inst.member.bark()  # mypy: "Animal" has no attribute "bark"
    inst.member.purr()  # mypy: "Animal" has no attribute "purr"

    inst.member = cat
    reveal_type(inst.member)  # mypy: Revealed type is 'Animal'
    inst.member.run()  # mypy: "Animal" has no attribute "run"
    inst.member.bark()  # mypy: "Animal" has no attribute "bark"
    inst.member.purr()  # mypy: "Animal" has no attribute "purr"

    inst.member = dog
    reveal_type(inst.member)  # mypy: Revealed type is 'Dog'
    inst.member.run()  # mypy: no error
    inst.member.bark()  # mypy: no error
    inst.member.purr()  # mypy: "Dog" has no attribute "purr"

    inst.member = cat_or_dog
    reveal_type(inst.member)  # mypy: Revealed type is 'Dog' !!!!
    inst.member.run()  # mypy: no error
    inst.member.bark()  # mypy: no error
    inst.member.purr()  # mypy: "Dog" has no attribute "purr"

    inst.member = cat
    reveal_type(inst.member)  # mypy: Revealed type is 'Dog' !!!!
    inst.member.run()  # mypy: no error
    inst.member.bark()  # mypy: no error !!!!
    inst.member.purr()  # mypy: "Dog" has no attribute "purr" !!!!
