from typing import Union, Tuple


def get_tuple() -> Union[Tuple[int, int], Tuple[None, None]]:
    return (1, 2)


def process_tuple(one, two, flag=False):
    print(one, two, flag)


process_tuple(*get_tuple(), flag=True)
