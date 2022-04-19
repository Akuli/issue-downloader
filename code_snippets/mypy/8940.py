from typing import Union, Dict, List, Literal

firstset = Union[Literal['a'], Literal['b'], Literal['c']]
secondset = Union[Literal['d'], Literal['e'], Literal['f']]

firstdict: Dict[firstset, int] = {'a': 2}
seconddict: Dict[secondset, float] = {'d': 3.0}

firstlist: List[firstset] = ['a', 'b', 'c']
secondlist: List[secondset] = ['d', 'e', 'f']

def printit(key: Union[Literal['a'], Literal['b'], Literal['c'],
                       Literal['d'], Literal['e'], Literal['f']]):
    if key in firstdict:
        reveal_type(key) # Union[Literal['a'], Literal['b'], Literal['c'], Literal['d'], Literal['e'], Literal['f']]'
    if key in seconddict:
        reveal_type(key) # Union[Literal['a'], Literal['b'], Literal['c'], Literal['d'], Literal['e'], Literal['f']]'

    if key in firstlist:
        reveal_type(key) # Union[Literal['a'], Literal['b'], Literal['c'], Literal['d'], Literal['e'], Literal['f']]'
    if key in secondlist:
        reveal_type(key) # Union[Literal['a'], Literal['b'], Literal['c'], Literal['d'], Literal['e'], Literal['f']]'

    if key == 'a' or key == 'b' or key == 'c':  # this one works
        reveal_type(key)  # 'Union[Literal['a'], Literal['b'], Literal['c']]' 
