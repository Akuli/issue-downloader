def foo() -> List[int]:
    listings = None
    if 2 != 2:
        listings = list()
        listings.append(1)
    return listings

def foo() -> List[int]:
    listings = None
    if 2 != 2:
        listings = [1]
    return listings
