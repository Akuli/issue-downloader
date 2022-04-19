def split_int_string(digits: str, *at: int) -> List[int]:
    """
    Split a string at given indices and parse the parts to int.
    """
    # Make a canonical representation.
    split: List[int] = sorted(at)
    if not split or split[0] != 0:
        split.insert(0, 0)
    if split[-1] != len(digits):
        split.append(len(digits))
    return [int(digits[split[i - 1] : split[i]]) for i in range(1, len(split))]
