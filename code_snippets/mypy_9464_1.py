array: ndarray

# note: Revealed type is 'builtins.int*'
reveal_type(argmax(array, axis=None))

# error: Cannot infer type argument 1 of "argmax"
# note: Revealed type is 'Any'
reveal_type(argmax(array, axis=0))

