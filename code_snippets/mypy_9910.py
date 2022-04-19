from typing import Final, final

class Parent:
    __foo: Final[int] = 0

    @final
    def __bar(self) -> None:
        pass

class Child(Parent):
    __foo: Final[int] = 1  # error: Cannot override final attribute "__foo" (previously declared in base class "Parent")

    @final  # error: Cannot override final attribute "__bar" (previously declared in base class "Parent")
    def __bar(self) -> None:
        pass
