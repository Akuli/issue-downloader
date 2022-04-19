from typing import Generic, TypeVar, TYPE_CHECKING

L = TypeVar('L')
R = TypeVar('R')

if TYPE_CHECKING:  # type declarations

    class Either(Generic[L, R]): pass
    Left = Either[L, None]
    Right = Either[None, R]

else:  # runtime implementation

    class Either(): pass
    class Left(Either): pass
    class Right(Either): pass


# type checking features
a: Left[int] 
b: Either[int, None]

a = b  # typechecks
b = a  # typechecks 

# runtime features
isinstance(Left(), Left)  #works at runtime 
isinstance(Left(), Either)  #works at runtime
