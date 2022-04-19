from typing import Iterable, Union

def as_bytes(data: Union[bytes, Iterable[bytes]]) -> bytes:
    """Return bytes as is; "flatten" iterable of bytes."""
    if isinstance(data, bytes):
        return data
    elif isinstance(data, Iterable):
        return b''.join(data)
    else:
        raise TypeError

from typing import Iterable, Union

def as_bytes(data: Union[bytes, Iterable[bytes]]) -> bytes:
    if isinstance(data, bytes):
        return data
    # note the redundant "and not ..." clause here -v
    elif isinstance(data, Iterable) and not isinstance(data, bytes):
        return b''.join(data)
    else:
        raise TypeError
