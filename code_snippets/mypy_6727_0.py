from typing import Tuple, Dict, Any


def exec(args: Tuple, kwargs: Dict[str, Any]):
    action_id = 0
    action_name = "exec"
    _command_fallback(*args, __action_id=action_id,
                      __action_name=action_name, **kwargs)


def _command_fallback(self, *args, __action_id: int, __action_name: str, **kwargs) -> str:
    print(args, __action_id, __action_name, kwargs)
    return "Success."
