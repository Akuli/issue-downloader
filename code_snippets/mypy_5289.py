#!/usr/bin/python2.7
from typing import Dict, Set  # noqa
x = {}  # type: Dict[str, Set[str]]
z = x[''] = set()  # okay
x[''] = y = set()  # fail: Incompatible types in assignment (expression has type "Set[<nothing>]", target has type "Set[str]")
