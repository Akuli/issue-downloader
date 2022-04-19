from dataclasses import dataclass

@dataclass
class Foo: ...

reveal_type(Foo.__eq__)  # Revealed type is "def (builtins.object, builtins.object) -> builtins.bool"
