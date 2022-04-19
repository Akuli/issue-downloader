class Base:
	def __init__(self, value):
		self._value = value

	@property
	def value(self):
		return self._value

class Sub(Base):
	@Base.value.setter
	def value(self, value):
		self._value = value

class Base:
	def __init__(self, value):
		self._value = value

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value

class Sub(Base):
	@Base.value.setter
	def value(self, value):
		self._value = value
