
try:
    from emoji import emojize
    reveal_type(emojize)
except ModuleNotFoundError:
    def emojize(string: str, use_aliases=False, delimiters=(':', ':'), variant=None, language='en'):
        return string
    reveal_type(emojize)
