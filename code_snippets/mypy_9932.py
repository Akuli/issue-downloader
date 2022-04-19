from typing import List
foo: "List"[int] = [1] # Accepted by mypy but generates runtime error
