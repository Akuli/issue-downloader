from unittest import mock
import subprocess


def foo() -> None:
    with mock.patch.object(
        subprocess,
        "Popen",
        **{"return_value.communicate.side_effect": KeyboardInterrupt}
    ):
        pass
