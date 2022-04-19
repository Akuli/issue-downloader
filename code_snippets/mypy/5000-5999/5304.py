from typing import Iterable, Dict, List, Sequence

# error: Incompatible types in assignment (expression has type "Tuple[List[Tuple[str, str]]]", variable has type "Iterable[List[Iterable[str]]]")
fields1: Sequence[List[Sequence[str]]] = ([('one', 'two')],)

# error: Incompatible types in assignment (expression has type "Tuple[Dict[str, Tuple[str, str]]]", variable has type "Iterable[Dict[str, Iterable[str]]]")
fields2: Sequence[Dict[str, Sequence[str]]] = ({'fields': ('one', 'two')},)

# It work normal
fields3: Sequence[Sequence[str]] = (('one', 'two'),)

# It also work normal
fields4: Dict[str, Sequence[str]] = {'fields': ('one', 'two')}

