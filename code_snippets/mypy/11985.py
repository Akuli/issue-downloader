#!/usr/bin/env python3

from collections.abc import Iterable
from typing import Optional
import os

def min_direntry_good(
        fs: 'Iterable[os.DirEntry[str]]'
) -> 'Optional[os.DirEntry[str]]':
    r = min(fs, default=None, key=lambda x: x.stat().st_mtime)
    return r

def min_direntry_bad(
        fs: 'Iterable[os.DirEntry[str]]'
) -> 'Optional[os.DirEntry[str]]':
    return min(fs, default=None, key=lambda x: x.stat().st_mtime)
