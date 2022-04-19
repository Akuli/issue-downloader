#!/usr/bin/env python3

from typing import (
	Any,
	Dict,
	Optional,
)

def required_int() -> int:
	x: Dict[str, Any] = {
		"id": "12345",
	}

	return x.get("id")

def optional_int() -> Optional[int]:
	x: Dict[str, Any] = {
		"id": "12345",
	}

	return x.get("id")
