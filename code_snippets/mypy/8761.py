from typing import Union, List, Literal, overload

class One:
    pass

class Two:
    pass

@overload
def func(x: Literal[False]) -> List[Two]:
    ...

@overload
def func(x: Literal[True]) -> List[Union[Two, One]]:
    ...

# actual definition typed with the most inclusive type
def func(x: bool) -> List[Union[Two, One]]:
    # instead of the code below, this can be just 'return []' or 'pass'
    # all 3 cases cause the same error
    if x:
        return [Two(), One()]
    else:
        return [Two()]
