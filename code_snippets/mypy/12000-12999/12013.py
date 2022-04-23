from typing import Callable, Generator


class Parent:
    def method_without(self) -> "Parent":
        ...

    def method_with(self, param: str) -> "Parent":
        ...


class Child(Parent):
    method_without: Callable[["Child"], "Child"]
    method_with: Callable[["Child", str], "Child"]

no_implicit_optional = True
scripts_are_modules = True
warn_unused_ignores = True
show_error_codes = True
