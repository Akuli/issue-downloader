from dataclasses import dataclass
from typing import Hashable


@dataclass
class SusDataclass:
    b = "AMONGUS"


h: Hashable = SusDataclass()  # SUS ALERT!

d = {
    SusDataclass(): 1  # SUS ALERT! fails at runtime
}
