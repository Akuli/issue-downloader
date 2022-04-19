
from typing import Protocol


class Person(Protocol):
    first_name: str

    def greeting(self, message: str) -> str:
        ...


class FrenchPerson(Person):
    prenom: str

    def __init__(self, name: str):
        self.prenom = name

    def salutation(self, message: str) -> str:
        return f"{message} {self.prenom}"


def print_person(person: Person) -> str:
    return person.greeting(message="Je m'appelle")


def main():
    fp = FrenchPerson(name='Henri')
    response = print_person(fp)
    print(response)
