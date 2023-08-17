from typing import Union
from abc import ABC, abstractmethod


class VolumeFactorCorrelation(ABC):
    @staticmethod
    @abstractmethod
    def calc(
        pressure: Union[float, int],
        temperature: Union[float, int],
        bubble_point_pressure: Union[float, int],
        max_solubility: Union[float, int],
        saturated_fvf: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        pass
