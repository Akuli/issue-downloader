from abc import ABCMeta, abstractmethod
from typing_extensions import overload, ParamSpec
from typing import TypeVar, Sequence, Optional, Callable

PResourceParams = ParamSpec('PResourceParams')
TResource = TypeVar('TResource', bound='Resource', covariant=True)

# Multiple implementations of Resource will exist, but
# a small set of construction-time parameters are guaranteed
# to be supported by all implementations.
class Resource(metaclass=ABCMeta):

    @overload
    def __init__(self, pathname: str):
        ...

    @overload
    def __init__(self, *, path: Sequence[str], name: str):
        ...

    @abstractmethod
    def __init__(
        self,
        pathname: Optional[str] = None,
        *,
        path: Optional[Sequence[str]] = None,
        name: Optional[str] = None,
    ):
        ...

# It's also intended for other, more specialized base ABCs to exist,
# at a conceptual level.
class AnotherResourceRoot(Resource, metaclass=ABCMeta):
    ...

# A Provider will select a suitable Resource implementation
# based on conditions internal to its implementation.
# The intention is to validate the small subset of constructor
# parameters that are supported by all resource implementations,
# and complement them with defaults, or other parameters that
# must be injected by the provider implementation.
class ResourceProvider(metaclass=ABCMeta):
    
    # resource_type is explicitly a callable so that PResourceParams
    # can be captured, and some type safety regarding this default
    # set of parameters can be enforced. It also allows to return the
    # exact type (or base ABC) as requested.
    def resource(
        self,
        resource_type: Callable[PResourceParams, TResource],
        *args: PResourceParams.args,
        **kwargs: PResourceParams.kwargs,
    ) -> TResource:
        ...

def main(provider: ResourceProvider):
    # Unfortunately, mypy doesn't seem to understand the __init__
    # overloads. Errors in the next line:
    #
    #  > error: Unexpected keyword argument "path" for "resource" of "ResourceProvider"
    #  > error: Unexpected keyword argument "name" for "resource" of "ResourceProvider"
    #
    # mypy does understand/recognize, however:
    #
    # 1. The @abstractmethod __init__ in Resource, if I remove all overloads; and
    # 2. The first overload only; you can swap overload positions to make it work,
    #    but it's not the desired situation.
    #
    resource = provider.resource(
        AnotherResourceRoot,
        #'abc/def/ghi.def',
        path=['abc', 'def'],
        name='ghi.def',
    )
    reveal_type(resource)  #  => Resource
