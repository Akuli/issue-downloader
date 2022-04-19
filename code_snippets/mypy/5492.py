from typing import List, Sequence, cast


class A:
    pass


class B1(A):
    pass


class B2(A):
    pass


# ok
list1: List[A] = [A()] * 10
# ok
list2: List[A] = [B1()] * 10
list2 += [B2()] * 10
# error!
list3: List[A] = [B1()] * 10 + [B2()] * 10
# error!
seq3: Sequence[A] = [B1()] * 10 + [B2()] * 10

# ok, but looks weird
list4: List[A] = [cast(A, B1())] * 10 + [B2()] * 10
