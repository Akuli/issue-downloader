from typing import List, Tuple


def get_point_as_list() -> List[int]:
    return [1, 2]


def point_to_tuple(pt: List[int]) -> Tuple[int, int]:
    assert len(pt) == 2
    return tuple(pt)


if __name__ == "__main__":
    l = get_point_as_list()
    p = point_to_tuple(l)
    print(repr(p))
