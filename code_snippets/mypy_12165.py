from typing import TypeGuard, _T, Callable

class Sus:
    def fake_tasks(sus, where: str) -> None: ...

def is_sus(it: object) -> TypeGuard[Sus]: ...

def run(fn: Callable[[object], _T]) -> None: ...

run(is_sus)  # error: Argument 1 to "run" has incompatible type "Callable[[object], TypeGuard[Sus]]"; expected "Callable[[object], Sus]"
