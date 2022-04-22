T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")

@dataclass
class FunctionRelation(Generic[T1, T2, T3]):
    func1: Callable[[T1], T2]
    func2: Callable[[T2], T3]

def func_str_int(x: str) -> int:
    return int(x)

def func_int_str(x: int) -> str:
    return str(x)

def func_str_str(x: str) -> str:
    return x

FunctionRelation(func1=func_str_int, func2=func_int_str)  # OK
FunctionRelation(func1=func_str_int, func2=func_str_str)  # Expected error - Cannot infer T2

relations: list[FunctionRelation[Any, Any, Any]] = []

def append_to_list(relation: FunctionRelation[T1, T2, T3]) -> None:
    relations.append(relation)

append_to_list(FunctionRelation(func1=func_str_int, func2=func_int_str))  # OK
append_to_list(FunctionRelation(func1=func_str_int, func2=func_str_str))  # Incorrectly accepted by Mypy!
relation = FunctionRelation(func1=func_str_int, func2=func_str_str)  # Expected error
append_to_list(relation)

@dataclass
class D(Generic[T1, T2, T3]):
    func1: Callable[[T1], T2]
    func2: Callable[[T2], T3]
