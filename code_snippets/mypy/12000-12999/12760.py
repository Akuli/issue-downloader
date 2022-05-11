from typing import Set
from zoneinfo import available_timezones

x = {"UTC"}


def error() -> Set[str]:
    return available_timezones() - set.union(x)


def ok() -> Set[str]:
    a, b = available_timezones(), set.union(x)
    return a - b
