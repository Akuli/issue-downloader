
from typing import (
	Dict,
	Optional,
)

def check1(x: Optional[str]) -> str:
	assert x  # x: str

	return x  # x: str

def check2(x: Optional[str]) -> str:
	assert x  # x: str

	x_map: Dict[str, str] = {
		"x": "y"
	}
	x = x_map.get(x, x)  # x: Optional[str] ??

	return x  # x: Optional[str] ??

def check3(x: Optional[str]) -> str:
	assert x  # x: str

	x_map: Dict[str, str] = {
		"x": "y"
	}
	x = x_map.get(x, x)  # x: Optional[str] ??

	assert x  # x: str

	return x  # x: str
