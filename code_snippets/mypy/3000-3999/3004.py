import typing
class A:
    @property
    def f(self) -> int:
        return 1
    @f.setter  # Possible error for defining a setter that doesn't accept the type the @property returns
    def f(self, x: str) -> None:
        pass
a = A()
a.f = ''  # Possibly not an error, but currently mypy gives an error
a.f = 1  # Certainly should be an error, unless we disallowed 
         # defining the setter this way in the first place.
reveal_type(a.f)  # E: Revealed type is 'builtins.int'
