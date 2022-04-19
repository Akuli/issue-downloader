from typing import List

global_var = [1, 2, 3]
global_var_annotated: List[int] = [1, 2, 3]
reveal_locals()

def foo():
    local_var = [1, 2, 3]
    local_var_annotated: List[int] = [1, 2, 3]
    reveal_locals()
