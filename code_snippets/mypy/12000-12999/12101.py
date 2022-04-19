from typing import Generic, TypeVar
from tjax._src.fixed_point.base import IteratedFunctionBase

State = TypeVar('State')
Parameters = TypeVar('Parameters')
Trajectory = TypeVar('Trajectory')


class SimpleScan(IteratedFunctionBase[Parameters, State, Trajectory, State],
                 Generic[Parameters, State, Trajectory]):
    pass

class EncodingSampler(SimpleScan[int, int, int]):
    pass

e = EncodingSampler()
reveal_type(e.sample_trajectory)  # "F`-`"!!
