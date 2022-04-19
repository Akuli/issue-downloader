from typing import Mapping, Hashable, Any, Union, Generic, TypeVar, overload, Dict

S1 = TypeVar("S1")


class A(Generic[S1]):
    # fails
    def myfun2(self, m: Union[Mapping[Any, Hashable], Hashable]):
        pass

    # Split the Union into two overloads works
    @overload
    def myfun3(self, m: Mapping[Any, Hashable]):
        ...

    @overload
    def myfun3(self, m: Hashable):
        ...

    def myfun3(self, m: Union[Mapping[Any, Hashable], Hashable]):
        pass

    # Use Dict instead of Mapping works
    def myfun4(self, m: Union[Dict[Any, Hashable], Hashable]):
        pass

    # Use Union[int, str] instead of Hashable works
    def myfun5(self, m: Union[Mapping[Any, Union[int, str]], Union[int, str]]):
        pass


a: A = A()
a.myfun2({1: 1})
a.myfun2("abc")
a.myfun3({1: 1})
a.myfun3("abc")
a.myfun4({1: 1})
a.myfun4("abc")
a.myfun5({1: 1})
a.myfun5("abc")
