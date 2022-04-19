def find1(name: str):
    return next(
        filter(
            lambda animal: animal.upper() == name,
            animals,
        ),
        None,
    )
