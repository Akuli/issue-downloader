from typing import Any
        
class Linear:
    def __init__(self, **kwargs) -> None:
        pass

class QatLinear(Linear):
    def __init__(self, qconfig=None):
        pass

def f(x: Any):
    if type(x) in [Linear, QatLinear]:
        pass
