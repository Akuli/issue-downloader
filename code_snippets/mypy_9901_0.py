from collections import namedtuple

class EmployeeRecord(namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')):
    
	def is_junior():
		return self.age < 18
