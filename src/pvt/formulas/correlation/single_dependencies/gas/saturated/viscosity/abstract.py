from typing import Union
from abc import ABC, abstractmethod


class ViscosityCorrelation(ABC):
    @classmethod
    @abstractmethod
    def calc(
        cls,
        temp: Union[float, int],
        dens_gas_standard: Union[float, int],
        dens_gas: Union[float, int],
        volume_factor: Union[float, int],
    ) -> Union[float, int]:
        pass
