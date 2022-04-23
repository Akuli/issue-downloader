from typing import Optional, Type, Any, TypeVar
T = TypeVar('T')
def structure(obj: Any, type: Type[T]) -> T:...

reveal_type(structure('foo', str))  #  Revealed type is 'builtins.str*'
reveal_type(structure('foo', Optional[str]))  # Revealed type is 'Any'

@typing.castlike
def structure(obj: Any, type: Type[T]) -> T:...
