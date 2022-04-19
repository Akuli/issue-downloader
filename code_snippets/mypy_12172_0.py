class Translation:
	def __init__(self, message: str):
		self.message = message

	def __str__(self) -> str:
		translate = _
		if translate is Translation:
			return self.message
		return translate(self.message)

	@classmethod
	def install(cls):
		import builtins
		builtins._ = cls


Translation.install()

s = _('something')
print(s)
