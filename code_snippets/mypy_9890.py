from typing import Optional, List


list_with_none: List[Optional[int]] = [None, 1, 2]


filtered = filter(lambda v: v is not None, list_with_none)
reveal_type(filtered)
# Revealed type is 'typing.Iterator[Union[builtins.int, None]]'

list_of_tuples: List[Tuple[Optional[int], Optional[int]]]
filter(lambda v: v[0] is not None and v[1] is not None, list_of_tuples)
# would become `Iterator[Tuple[int, int]]`

