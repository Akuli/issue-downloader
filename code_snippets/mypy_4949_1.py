T = TypeVar('T', bound = A)

def check_subtype(instance: A, instance_type: Type[T]) -> Optional[T]:
    if isinstance(instance, instance_type):
      return instance
    return None
