class Animal:
    name: Literal["animal"]
    n_legs: int

class Plant:
    name: Literal["plant"]

def get_n_legs(item: Union[Animal, Plant]):
    if item.name == "animal" and item.n_legs > 6:    # This fails mypy with union-attr for n_legs in Plant
        return "Many" 
