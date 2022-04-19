list_of_tuples: List[Tuple[Optional[int], Optional[int]]]
filter(lambda v: v[0] is not None and v[1] is not None, list_of_tuples)
# would become `Iterator[Tuple[int, int]]`
