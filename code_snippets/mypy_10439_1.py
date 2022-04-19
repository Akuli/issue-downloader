def func_1(address: Address) -> Optional[float] :
    ...

def func_2(addresses: Tuple[Addresses, ...]) -> Optional[Tuple[float, ...]]:
    ordered_list = []
    for address in addresses:
        value = func_1(address)
        if value is not None:
            ordered_list.append(value)
        else:
            return None
    return tuple(ordered_list)
