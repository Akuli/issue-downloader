from typing import TYPE_CHECKING

class A: ...
class B: ...
class C(A if TYPE_CHECKING else B): ...  # error: Invalid base class  [misc]
