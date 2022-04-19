from typing import *

class Unreachable:
	def member_function(self) -> None:
		self.path: Optional[str] = None
		self.other()
		if self.path:
			print(self.path)
			
	def other(self) -> None:
		self.path = 'hi'
		
Unreachable().member_function()
