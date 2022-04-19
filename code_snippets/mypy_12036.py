from typing import Optional, Union, Text


def ensure_unicode1(t: Optional[Union[str, Text]]) -> Optional[Text]:
    if t is None:
        return None
    elif isinstance(t, bytes):
        return t.decode('utf-8')
    return t


def ensure_unicode2(t: Optional[Union[str, Text]]) -> Optional[Text]:
    if t is None:
        return None
    return t.decode('utf-8') if isinstance(t, bytes) else t   # <--- line 15
