from typing import TypeVar, Tuple, Optional

Result = TypeVar("Result")

WorkerResult = Tuple[
    Optional[Result],         # <- "No Anys on this line!"
    Optional[BaseException],  # <- "No Anys on this line!"
    str                       # <- "No Anys on this line!"
]

WorkerResult = Tuple[Optional[Result], Optional[BaseException], str]

