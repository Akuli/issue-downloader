from typing import Union
def maybe_convert_to_int(x: Union[float,int]) -> Union[float,int]:
    '''Convert x from float to int if it can be done losslessly.'''
    if isinstance(x, float):
        # x must be a float here, so this is a legal operation, but
        # mypy still thinks its type is Union[float,int]
        assert isinstance(x, float)
        if x.is_integer():
            x = int(x)
    return x
