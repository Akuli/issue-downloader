x = [[], [1]]
for b in x:
    reveal_type(b) # error: Revealed type is 'builtins.object*'
    b + [1]  # error: Unsupported left operand type for + ("object")
