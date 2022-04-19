class ParentA:
    def get_description(self, s: str): ...


class ParentB:
    def get_description(self, i: int): ...


# This is a Liskov violation and needs to be ignored.
class ParentViolation(ParentA, ParentB):  # type: ignore
    ...


class ShouldBeIrrelevant:
    ...


# Inheriting from a violating parent, showing no error
class NoViolation(ParentViolation):
    ...


# Inheriting from a violating parent, but an extra class makes a violation appear
class SpuriousViolation(ParentViolation, ShouldBeIrrelevant):
    ...
