from typing import *


S = TypeVar("S")
T = TypeVar("T")


def map_or_else(func: Callable[[S], T], value: Optional[S], default: T) -> T:
    if value is None:
        return default
    return func(value)


# No mypy error
def func_1():
    data: Dict[str, List[str]] = {
        "items": [
            "a", "b", "c",
        ],
    }

    items = map_or_else(set, data.get("items"), None)

    if items is not None:
        print(items)



# Mypy error
def func_2(other_data: Dict[str, List[str]]):
    data: Dict[str, List[str]] = {
        "items": [
            "a", "b", "c",
        ],
    }

    items = map_or_else(set, data.get("items"), None)

    if items is not None:
        print(items)


# Mypy error
def func_2b(just_a_string: str):
    data: Dict[str, List[str]] = {
        "items": [
            "a", "b", "c",
        ],
    }

    items = map_or_else(set, data.get("items"), None)

    if items is not None:
        print(items)


# Mypy error
def func_3(data: Dict[str, List[str]]):
    items = map_or_else(set, data.get("items"), None)

    if items is not None:
        print(items)


# Mypy error
def func_3b(data: Dict[str, List[str]]):
    items: Optional[Set[str]] = map_or_else(set, data.get("items"), None)

    if items is not None:
        print(items)


def make_set(items: Iterable[T]) -> Set[T]:
    return set(items)


# Mypy error
def func_4(data: Dict[str, List[str]]):
    items = map_or_else(make_set, data.get("items"), None)

    if items is not None:
        print(items)


# Mypy error
def func_4b(data: Dict[str, List[str]]):
    make_set: Callable[[Iterable[T]], Set[T]] = set

    items: Optional[Set[str]] = map_or_else(make_set, data.get("items"), None)

    if items is not None:
        print(items)


# No mypy error
def func_5():
    data: Dict[str, List[str]] = {
        "items": [
            "a", "b", "c",
        ],
    }

    items = map_or_else(make_set, data.get("items"), None)

    if items is not None:
        print(items)


def make_set_2(items: Iterable[str]) -> Set[str]:
    return set(items)


# No mypy error
def func_6(data: Dict[str, List[str]]):
    items = map_or_else(make_set_2, data.get("items"), None)

    if items is not None:
        print(items)



if __name__ == "__main__":
    some_data: Dict[str, List[str]] = {
        "items": [
            "a", "b", "c",
        ],
    }

    func_1()
    func_2({})
    func_2b("")
    func_3(some_data)
    func_3b(some_data)
    func_4(some_data)
    func_4b(some_data)
    func_5()
    func_6(some_data)

