class WrongGenericImpl(GenericBase[str, int, str]):
    def first_step(self, pipeline_input: str) -> int:
        return len(pipeline_input)
