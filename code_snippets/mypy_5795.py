from typing import Optional, List, cast

things: Optional[List[int]] = None
others: List[int] = []

if things is not None:
    filtered = filter(lambda x: x in cast(List[int], things), others)
