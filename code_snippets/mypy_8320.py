from typing import Union, List, TypeVar

SomethingWithWs = Union[str, List['SomethingWithWs']]

T = TypeVar('T', bound=SomethingWithWs)


def remove_w(data: T) -> T:
    if isinstance(data, str):
        return data.replace('w', '')
    elif isinstance(data, list):
        return [remove_w(d) for d in data]
    else:
        raise TypeError()
