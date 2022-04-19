class ChoiceField(Field):
    def to_python(self, data: Optional[Any]) -> str: ...

class ModelChoiceField(ChoiceField):
    def to_python(self, data: Optional[Any]) -> Optional[Model]: ...  # type: ignore[override]
