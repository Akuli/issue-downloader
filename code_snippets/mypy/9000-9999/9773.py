# Returns `value` if it conforms to the specified type annotation using typechecker subtyping rules.
def trycast(typelike: TypeForm[T], value: object) -> Optional[T]: ...

# Returns whether the specified value can be assigned to a variable with the specified type annotation using typechecker subtyping rules.
def isassignable(value: object, typelike: TypeForm[T]) -> bool: ...
