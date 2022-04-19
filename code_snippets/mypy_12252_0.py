class FieldCategory(IntEnum):
	""" Names used to prefix the capture group name for a field.
	The enum's name is used to get a value of that category for a Body, or the substring of its name.
	The enum's value is used to sort display of multiple FieldGroups in the same Col.
	"""
	bnk = auto()
	num = auto()
	off = auto()

	def __init__(self, num):
		self.cap_name = f'cap_{self.name}'
		self.cap_str = attrgetter(f'type.cap_{self.name}')
		self.val_method: Callable[[OpndBody], FieldCatVal] = methodcaller(f'{self.name}_val')

	def get_val(self, body: Body):
		""" The computed value of the body for this category.
		It is a property of the body whose name depends on the body's type.
		"""
		# The following line crashes mypy!
		assert isinstance(body, bodies.Body)	# type:ignore         [ line 986 with INTERNAL ERROR ]
		return self.val_method(body)
	
from solver import  bodies
	
