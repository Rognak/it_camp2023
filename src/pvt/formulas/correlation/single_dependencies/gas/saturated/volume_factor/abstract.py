from typing import Union
from abc import ABC, abstractmethod


class VolumeFactorCorrelation:
    FVF_k1 = 350.958

    @classmethod
    @abstractmethod
    def calc(
        cls,
        temp: Union[float, int],
        pres: Union[float, int],
        supercompressibility: Union[float, int] = 1,
    ) -> Union[float, int]:
        pass
