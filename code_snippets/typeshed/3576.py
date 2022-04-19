from typing import Iterator, Mapping

class MyMap:
    def __getitem__(self, key: str) -> int:
        return 0
    def __iter__(self) -> Iterator[str]:
        return iter([])
    def __len__(self) -> int:
        return 0
    def __contains__(self, key: object) -> bool:
        return False

def foo(x: Mapping[str, int]) -> None:
    pass

foo(MyMap())  # error: Argument 1 to "foo" has incompatible type "MyMap"; expected "Mapping[str, int]"
