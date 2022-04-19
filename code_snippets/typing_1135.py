from typing import Callable, Generic, Any
from typing_extensions import ParamSpec

_P = ParamSpec("_P")

class Job(Generic[_P]):
    def __init__(self, target: Callable[_P, None]) -> None:
        self.target = target

def call_job(
    job: Job[...],
    *args: Any
) -> None:
    job.target(*args)
