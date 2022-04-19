from returns.curry import curry

class Test(object):
    @curry
    def __init__(self, a: int, b: str) -> None:
        ...

    @curry
    def some(self, a: int, b: str) -> None:
        ...

t: Test

# Works fine!
reveal_type(t.some)
# => Revealed type is 'Overload(def () -> Overload(def (a: builtins.int, b: builtins.str), def (a: builtins.int) -> def (b: builtins.str)), def (a: builtins.int) -> def (b: builtins.str), def (a: builtins.int, b: builtins.str))'

# Modifies the return type from our plugin.
reveal_type(Test)
# => Revealed type is 'Overload(def () -> ex.Test, def (a: builtins.int) -> ex.Test, def (a: builtins.int, b: builtins.str) -> ex.Test)'

reveal_type(Test)
# => Revealed type is 'Overload(def () -> ex.Test, def (a: builtins.int) -> ex.Test, def (a: builtins.int, b: builtins.str) -> ex.Test)'
