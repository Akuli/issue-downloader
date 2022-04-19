_SUPPORTED_LITERAL_OPERATIONS: Final = {
    int: ('+', '-', '*', '//'),  # `/` returns `float`
    str: ('+',),
    bool: ('and', 'or'),
}
