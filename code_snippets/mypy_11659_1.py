import pytest
from subprocess import CalledProcessError

with pytest.raises((TypeError, CalledProcessError)) as exc_info:
    pass
# error: Need type annotation for "exc_info"
# error: Argument 1 to "raises" has incompatible type "Tuple[Type[TypeError], Type[CalledProcessError]]"; expected "Union[Type[<nothing>], Tuple[Type[<nothing>], ...]]"
