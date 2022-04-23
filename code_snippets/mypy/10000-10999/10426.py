from typing import Optional

animals = ["cow"]


def find1(name: str) -> Optional[str]:
    return next(
        filter(
            lambda animal: animal.upper() == name,
            animals,
        ),
        None,
    )

def find1(name: str):
    return next(
        filter(
            lambda animal: animal.upper() == name,
            animals,
        ),
        None,
    )
