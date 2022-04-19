from dataclasses import dataclass
from typing import Literal


@dataclass
class Data:
    state: Literal["on", "off"]

    def set_state(self, state: Literal["on", "off"]):
        self.state = state


def test_func():
    obj = Data("on")
    assert obj.state == "on"

    obj.set_state("off")
    #   ^^^^^^^^^^^^^^^^ mutation happens here
    assert obj.state == "off"
    #      ^^^^^^^^^
    # mypy: Non-overlapping equality check (left operand type: "Literal['on']", right operand type: "Literal['off']")
