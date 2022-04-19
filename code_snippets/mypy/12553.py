#!/usr/bin/env python3

import socket
from enum import Enum
from typing import Iterator, Type, TypeVar

_E = TypeVar("_E", bound=Enum)

def enum_iter(cls: Type[_E]):
    return iter(cls)

for value in enum_iter(socket.SocketKind):
    print(value)
