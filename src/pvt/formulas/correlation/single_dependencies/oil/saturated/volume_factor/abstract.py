from typing import Union
from abc import ABC, abstractmethod


class VolumeFactorCorrelation(ABC):
    @classmethod
    @abstractmethod
    def calc(
        cls,
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
        solubility: Union[float, int],
    ) -> Union[float, int]:
        pass
