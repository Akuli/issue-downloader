from typing import Type, Any

def generate_str(cls: Type) -> Type:
    """
    Class decorator that auto generates __str__().
    :param cls: class to modify
    :return: modified class
    """
    def __str__(self) -> str:
        return _pretty_print_obj(self)

    cls.__str__ = __str__
    return cls
