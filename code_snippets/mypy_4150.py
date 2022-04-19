#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

from typing import Iterable

def update(ccc: dict, meta: dict) -> dict:
    foo = dict(ccc)
    foo.update(meta)
    return foo

def reduce_func(configs: Iterable[dict]) -> dict:
    output = dict(reduce(update, configs, {})) # type: dict
    return output

print(reduce_func([{"a": 1}, {"b": 2}]))

