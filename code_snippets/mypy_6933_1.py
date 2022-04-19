class Collection(Generic[T]):
    "Collection of elements"

    def apply(self, op: Transform[T, OutT]) -> 'Collection[OutT]':
        """
        Apply the this Collection to a Transform and produce a new 
        output Collection
        """
