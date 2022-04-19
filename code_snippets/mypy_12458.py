class InstrValCol(Col[ColKey, ValType], ColAttrsBase, metaclass=CacheMeta):
	...
	class LookupResultTup(NamedTuple):
		status : RowKeyStatus
		value : Optional[ValType] = None

		def __repr__(self):
			repr = self.status.name
			if self.value is not None: repr += f' {self.value}'
			return repr
