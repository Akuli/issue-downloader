from typing import Protocol

class Factory(Protocol):
    def __call__(self) -> Result:
        ...

class Result(Protocol):
    a: int
    
class BadImplementation:
    ...

def bad_implementation() -> BadImplementation:
    ...

something: Factory = BadImplementation  # no error
something_else: Factory = bad_implementation  # yes error
