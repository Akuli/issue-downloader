class PersonWrapper:
    def __init__(self, person: Person, default: Any = '') -> None:
        self.person = person
        self.default = default

    def __getattr__(self, attribute: str) -> Any:
        return getattr(self.person, attribute, self.default)

def print_person(original_person: Person) -> None:
    person = PersonWrapper(original_person)
    # This attribute might be missing from the original person object.
    print(f'  Username: {person.username}')
    person = original_person
    # Only print this if the attribute exists.
    phone = getattr(person, 'phoneNumber', None)
    if phone:
        print(f'    Phone: {phone}')
