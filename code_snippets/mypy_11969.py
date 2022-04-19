from dataclasses import dataclass


@dataclass
class Foo:
    value: int
    modified: bool = False

    def update(self) -> None:
        self.value += 1
        self.modified = True


foo = Foo(42)
assert not foo.modified
foo.update()
assert foo.modified
print("Reached")
