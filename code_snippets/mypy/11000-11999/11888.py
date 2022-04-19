i: int = 1
s: str = 'hi'
i is s  # error: Non-overlapping identity check (left operand type: "int", right operand type: "str")
if i is None: # ok
   ...
