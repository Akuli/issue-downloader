def function2(obj: T) -> T:  # unexpected behaviour:
    if isinstance(obj, A) or isinstance(obj, B):
        pass
    return obj  # mypy has forgotten that obj is of type T
