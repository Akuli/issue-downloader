class PersonWrapper:
    def __init__(self, person: Person, default: Any = '') -> None:
        self.person = person
        self.default = default

    def __getattr__(self, attribute: str) -> Any:
        return getattr(self.person, attribute, self.default)
