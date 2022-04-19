R = TypeVar("R")
FileCachedData = TypedDict('FileCachedData', {'mtime': float, 'size': int, 'value': R})
