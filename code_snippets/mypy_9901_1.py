from typing import NamedTuple

class EmployeeRecord(NamedTuple):
	name: Any
	age: Any
	title: Any
	department: Any
	paygrade: Any
	def is_junior(): ...
