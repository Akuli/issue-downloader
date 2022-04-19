from typing import TypeGuard, _T, Callable

class Sus:
    def fake_tasks(sus, where: str) -> None: ...

def is_sus(it: object) -> TypeGuard[Sus]: ...

def run(fn: Callable[[], _T]) -> _T: ...

crewmate: int

if run(lambda: is_sus(crewmate)):
    crewmate.fake_tasks("medbay")  # int" has no attribute "fake_tasks"
