def func_1(address: Address) -> Optional[float] :
    ...

def func_2(addresses: Tuple[Addresses, ...]) -> Optional[Tuple[float, ...]]:
    ordered_tuple = tuple(
        func_1(address)
        for address in addresses)
    return ordered_tuple if not None in ordered_tuple else None
