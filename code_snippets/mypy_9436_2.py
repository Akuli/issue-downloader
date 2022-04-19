
array: ndarray[bool_]
scalar: bool_

# note: Revealed type is 'op.bool_*'
reveal_type(scalar + scalar)

# error: Value of type variable "T1" of "__radd__" of "bool_" cannot be "ndarray[bool_]"  [type-var]
# note: Revealed type is 'op.ndarray*[op.bool_]'
reveal_type(array + scalar)

