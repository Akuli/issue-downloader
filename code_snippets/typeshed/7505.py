from typing import Union

print(isinstance(1, Union[str, int]))  # error: Argument 2 to "isinstance" has incompatible type "object"; expected "Union[type, UnionType, Tuple[Union[type, UnionType, Tuple[Any, ...]], ...]]"
