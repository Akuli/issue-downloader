def print_person(original_person: Person) -> None:
    person = PersonWrapper(original_person)
    # This attribute might be missing from the original person object.
    print(f'  Username: {person.username}')
    person = original_person
    # Only print this if the attribute exists.
    phone = getattr(person, 'phoneNumber', None)
    if phone:
        print(f'    Phone: {phone}')
