from typing import Optional, List


list_with_none: List[Optional[int]] = [None, 1, 2]


filtered = filter(lambda v: v is not None, list_with_none)
reveal_type(filtered)
# Revealed type is 'typing.Iterator[Union[builtins.int, None]]'
