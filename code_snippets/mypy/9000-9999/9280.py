from typing import TypedDict, Any, cast

class JSONTask(TypedDict, total=False):
    ...
    @staticmethod  # type: ignore
    def validate(d: Any) -> bool:
        ...
        return True
