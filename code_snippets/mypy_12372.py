class A:
    def foo(self) -> int: pass

class B(A):
    def foo(self) -> str: pass  # type: ignore[override]

class C(B):
    def foo(self) -> str: pass

class ChoiceField(Field):
    def to_python(self, data: Optional[Any]) -> str: ...

class ModelChoiceField(ChoiceField):
    def to_python(self, data: Optional[Any]) -> Optional[Model]: ...  # type: ignore[override]

