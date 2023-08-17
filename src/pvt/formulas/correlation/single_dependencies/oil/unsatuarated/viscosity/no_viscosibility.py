from abc import abstractmethod, ABC
from typing import Union
from pvt.formulas.correlation.single_dependencies.oil.unsatuarated.viscosity.abstract import (
    ViscosityCorrelation,
)


class NoViscosibility(ViscosityCorrelation):
    @classmethod
    @abstractmethod
    def calc(
        cls,
        pressure: Union[float, int],
        bubble_point_pressure: Union[float, int],
        bubble_point_viscosity: Union[float, int],
    ):
        return bubble_point_viscosity
