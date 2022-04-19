from typing import TypeVar, Generic
from abc import abstractmethod, ABC

K = TypeVar('K')


class Metric(ABC, Generic[K]):

    @abstractmethod
    def sum(self, other: "Metric[K]") -> "Metric[K]":
        pass


class MyFloatMetric(Metric[float]):
    def sum(self, other: "MyFloatMetric") -> "MyFloatMetric":
        return MyFloatMetric()

[mypy]

# Global settings
disallow_untyped_defs    = False
show_column_numbers      = True
show_error_codes         = True
strict_optional          = True
warn_no_return           = True
warn_redundant_casts     = True
# activate later
warn_unused_ignores      = False
ignore_missing_imports   = True

# Enable these over time
check_untyped_defs       = False
disallow_incomplete_defs = False
no_implicit_optional     = False
warn_return_any          = False
warn_unreachable         = False

