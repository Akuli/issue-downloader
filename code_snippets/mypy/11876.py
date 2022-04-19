from typing import Union, NoReturn

def func() -> Union[str, NoReturn]:
    return 'test'

func().lower()
