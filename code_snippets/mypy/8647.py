
from returns.pipeline import pipe
from returns.result import Result, Success, Failure, safe
from returns.pointfree import bind

def regular_function(arg: int) -> float:
 return float(arg)


def returns_container(arg: float) -> Result[str, ValueError]:
 if arg != 0:
      return Success(str(arg))
 return Failure(ValueError())



@safe
def also_returns_container(arg: str) -> str:
 return arg.lower()


transaction = pipe(
 regular_function,  # composes easily
 returns_container,  # also composes easily, but returns a container
 # So we need to `bind` the next function to allow it to consume
 # the container from the previous step.
 bind(also_returns_container),
)
result = transaction(1)  # running the pipeline
assert result == Success('1.0!')
