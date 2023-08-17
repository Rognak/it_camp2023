from typing import Union
from abc import ABC, abstractmethod


class DeadOilViscosityCorrelation(ABC):
    @classmethod
    @abstractmethod
    def calc(
        cls,
        temp: Union[float, int],
        dens_oil: Union[float, int],
    ) -> Union[float, int]:
        pass


class LiveOilViscosityCorrelation(ABC):
    @classmethod
    @abstractmethod
    def calc(
        cls,
        deed_viscosity: Union[float, int],
        solubility: Union[float, int],
    ) -> Union[float, int]:
        pass