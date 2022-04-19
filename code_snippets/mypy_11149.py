from typing import TypeVar, Union, List

T1 = TypeVar("T1")

def promote_list(item: Union[T1, List[T1]]) -> List[T1]:
    ...

exprs: List[int]
reveal_type(promote_list(exprs))  # error
# ex.py:9: note: Revealed type is "builtins.list[<nothing>]"
# ex.py:9: error: Argument 1 to "promote_list" has incompatible type "List[int]"; expected "List[<nothing>]"

reveal_type(promote_list(1))  # ok
# Revealed type is "builtins.list[builtins.int*]"
