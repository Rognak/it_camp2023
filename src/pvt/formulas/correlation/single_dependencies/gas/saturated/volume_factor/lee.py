from typing import Union
from pvt.formulas.correlation.single_dependencies.gas.saturated.volume_factor.abstract import (
    VolumeFactorCorrelation,
)


class Lee(VolumeFactorCorrelation):
    FVF_k1 = 350.958

    @classmethod
    def calc(
        cls,
        temp: Union[float, int],
        pres: Union[float, int],
        supercompressibility: Union[float, int] = 1,
    ) -> Union[float, int]:
        """
        :param temp: Температуры, К
        :param pres: Давления, Па
        :param supercompressibility: Коэффицент сверхсжимаемости
        :return: Объемный коэфицент м3 / м3
        """
        value = cls.FVF_k1 * supercompressibility * temp / pres
        return value
