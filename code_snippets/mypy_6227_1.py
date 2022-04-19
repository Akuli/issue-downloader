from typing import Iterable, Union

def as_bytes(data: Union[bytes, Iterable[bytes]]) -> bytes:
    if isinstance(data, bytes):
        return data
    # note the redundant "and not ..." clause here -v
    elif isinstance(data, Iterable) and not isinstance(data, bytes):
        return b''.join(data)
    else:
        raise TypeError
