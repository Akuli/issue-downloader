from collections import namedtuple

class EmployeeRecord(namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')):
    
	def is_junior():
		return self.age < 18

from typing import NamedTuple

class EmployeeRecord(NamedTuple):
	name: Any
	age: Any
	title: Any
	department: Any
	paygrade: Any
	def is_junior(): ...

class EmployeeRecord:
	def is_junior(): ...
