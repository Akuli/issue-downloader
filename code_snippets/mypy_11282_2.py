def handler():
    try:
        result = f()  # some function with Union[str, NoResult] return type
        ...  # in all lines in the try block Mypy could safely assume that result will be str
    except Exception as exc:
        ...  # here I'm not sure, but at least we could assume the type of exc variable? In case we've got a few other functions that could raise an exception in a try block, this could be a union of all NoResults in try block for which this exception is an ancestor.
