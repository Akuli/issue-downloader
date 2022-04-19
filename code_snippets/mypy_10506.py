from typing import ClassVar, List


class Seat(object):
    ...


class LeatherSeat(Seat):
    ...


class PlasticSeat(Seat):
    ...


class SomeBucket(Seat):
    ...


##############
# Failing Case 1
class TransportMedium(object):
    seats: ClassVar[List[Seat]] = []


class Car(TransportMedium):
    ...


class ElectricCar(Car):
    seats = [LeatherSeat()]


class ManufacturerCar(ElectricCar):
    # List item 0 has incompatible type "PlasticSeat"; expected "LeatherSeat"
    seats = [PlasticSeat()]


############
# Failing Case 2
class Train(TransportMedium):
    # Need type annotation for 'seats' (hint: "seats: List[<type>] = ...")
    seats = []


############
# Probably successful case
class Plane(TransportMedium):
    #  List item 0 has incompatible type "None"; expected "Seat"
    seats = [None]


################################
# Simple class var type checking works
class Base(object):
    class_var: ClassVar[str] = "this is a class var"


class Sub(Base):
    ...


class SubSub(Sub):
    # Incompatible types in assignment (expression has type "None", base class "Base" defined the type as "str")
    class_var = None


class Last(Sub):
    class_var = "should be OK"

[mypy]
ignore_missing_imports = True
warn_return_any = False

