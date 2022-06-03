from abc import ABC, abstractmethod
from typing import Mapping, TypedDict

PayloadType = Mapping[str, object]

class ArgumentType(TypedDict):
    name: str

class ReturnType(TypedDict):
    result: bool

class IHandle(ABC):

    @abstractmethod
    def do_handle(self, name: PayloadType) -> PayloadType:
        ...

class Handler(IHandle):

    def do_handle(self, name: ArgumentType) -> ReturnType:
        return {
            'result': True,
        }

handler = Handler()
name: ArgumentType = {'name': 'example'}
handler.do_handle(name)

