from abc import ABC
from typing import List
class MyBase(ABC):
    ...
class A(MyBase):
    ...
class B(MyBase):
    ...

def foo() -> None:
    txns: List[MyBase] = []
    reveal_type(txns)
    txn = txns[0]
    reveal_type(txn)
    assert isinstance(txn, A)
    reveal_type(txn)
    # This next line is optional.  Both will trigger the bug.
    # txn = [txn for txn in txns if False][0]
    reveal_type(txn)
    assert isinstance(txn, B)
    # Type checking seems to stop here. The reveal_types don't get printed
    reveal_type(txn)
    reveal_type(56)
    # And no error is printed about the assignment.
    txn = 67
