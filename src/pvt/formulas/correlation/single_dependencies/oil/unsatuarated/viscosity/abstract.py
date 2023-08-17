from abc import abstractmethod, ABC
from typing import Union


class ViscosityCorrelation(ABC):
    @classmethod
    @abstractmethod
    def calc(
        cls,
        pressure: Union[float, int],
        bubble_point_pressure: Union[float, int],
        bubble_point_viscosity: Union[float, int],
    ):
        pass
