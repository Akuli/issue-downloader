def blocking_sleep(t: float) -> None:
    assert_no_running_loop()
    time.sleep(t)

async def foo() -> None:
    blocking_sleep(10)

from mypy_extensions import Blocking

def blocking_sleep(t: float) -> Blocking[None]:
    assert_no_running_loop()
    time.sleep(t)
