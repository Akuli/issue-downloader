class Apple(object): ...

T_co = TypeVar('T_co', covariant=True)
A_co = TypeVar('A_co', bound=Apple, covariant=True)

class Action(Generic[T_co]): ...

class AppleAction(Generic[A_co], Action[A_co]): ...

if isinstance(action, AppleAction):
   reveal_type(action)
