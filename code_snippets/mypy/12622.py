from typing import Optional, TypeVar

class Parent:
    def copy(self):
        return self

MaybeParent = TypeVar("MaybeParent", bound=Optional[Parent])

def try_copy_works(parent: Optional[Parent]) -> Optional[Parent]:
    if parent is None:
        return None
    return parent.copy()

def try_copy_doesnt_work(parent: MaybeParent) -> MaybeParent:
    if parent is None:
        return
    # Item "object" of the upper bound "Optional[Parent]" of type variable "MaybeParent" has no attribute "copy"
    return parent.copy()

def try_copy_doesnt_work_either(parent: MaybeParent) -> MaybeParent:
    if parent is None:
        return
    # Incompatible types in assignment (expression has type "MaybeParent", variable has type "Parent")
    guarded_parent: Parent = parent
    return guarded_parent.copy()
