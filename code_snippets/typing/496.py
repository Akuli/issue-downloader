if __typing__:
    from typing import *
    T = TypeVar('T')
    UserId = NewType('UserId', int)
    ...  # etc.

def f(users: List[UserId]) -> Optional[UserId]:
    ...

# reveal_type(previous_result) is `builtins.int`
result: cast(UserId) = previous_result
