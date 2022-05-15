# Simulates a wrongly typed function in a types library (Redis get command)
def wrong_type_get() -> str|None:
	return "abc"
	
def get_int() -> int:
	value = wrong_type_get()
	assert isinstance(value, int) # type:ignore[unreachable]
	return value
