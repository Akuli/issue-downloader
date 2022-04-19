#!/usr/bin/env python3
from typing import Union, List, Optional

def test(a: Union[List[str], str, None] = None) -> Optional[List[str]]:
    if type(a) == str:
        a = [a]
    assert(type(a) != str)
    return a
