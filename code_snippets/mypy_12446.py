from typing import Literal

dest: Literal["tata", "tutu"]

for src in "tata", "tutu":
    dest = src

t = "tata", "tutu"
reveal_type(t)
reveal_type(t.__iter__())

