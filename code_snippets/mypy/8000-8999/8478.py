from typing import (
    TypeVar,
    List,
    Callable,
    Optional,
)

Task = TypeVar("Task")
Result = TypeVar("Result")


def run_tasks(
    tasks: List[Task], worker_fun: Callable[[Task], Result]
) -> List[Optional[Result]]:
    results: List[Optional[Result]] = []

    toggle: bool = True
    todo: Task
    for todo in tasks:
        toggle = not toggle

        if toggle:
            work_result: Result
            work_result = worker_fun(todo)
            results.append(work_result)
        else:
            results.append(None)

    return results


def test() -> None:
    def worker(d: int) -> Optional[int]:
        if d % 2 == 0:
            return None
        else:
            return d + 1

    output: List[Optional[Optional[int]]] = run_tasks(
        [1, 2, 2, 1], worker,
    )
    from pprint import pprint

    pprint(output)
    assert output == [None, None, None, 2]


test()

def test2() -> None:
    def worker(d: int) -> int:
        return d + 1

    output: List[Optional[int]] = run_tasks(
        [1, 2, 2, 1], worker,
    )
    from pprint import pprint

    pprint(output)
    assert output == [None, 3, None, 2]


test2()

