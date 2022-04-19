import dataclasses
from dataclasses import dataclass, InitVar
from functools import partial

dataclass_alias = dataclass
dataclass_partial = partial(dataclass, frozen=True)
dataclass_decorator = dataclass(frozen=True)

# 1. ok
@dataclass(frozen=True)
class X1:
    value: InitVar[bool] = None


# 2. ok
@dataclasses.dataclass(frozen=True)
class X2:
    default: InitVar[bool] = None


# 3. error: Incompatible types in assignment (expression has type "None", variable has type "InitVar[bool]")
@dataclass_alias(frozen=True)
class X3:
    default: InitVar[bool] = None


# 4. error: Incompatible types in assignment (expression has type "None", variable has type "InitVar[bool]")
@dataclass_partial
class X4:
    default: InitVar[bool] = None

# 5a. error: Too many arguments for "object"
# 5b. error: Incompatible types in assignment (expression has type "None", variable has type "InitVar[bool]")
@dataclass_partial()
class X5:
    default: InitVar[bool] = None


# 6. error: Incompatible types in assignment (expression has type "None", variable has type "InitVar[bool]")
@dataclass_decorator
class X6:
    default: InitVar[bool] = None
