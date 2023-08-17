from typing import Union
from pvt.formulas.correlation.single_dependencies.oil.saturated.volume_factor.abstract import (
    VolumeFactorCorrelation,
)


class Beggs(VolumeFactorCorrelation):
    FVF_k1 = 0.972
    FVF_k2 = 0.000147
    FVF_k3 = 5.614583333333334
    FVF_k4 = 2.25
    FVF_k5 = 574.5875
    FVF_k6 = 1.175

    @classmethod
    def calc(
        cls,
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
        solubility: Union[float, int],
    ) -> Union[float, int]:
        """
        :param temp: Температуры, К
        :param dens_oil: Плотности дегазированной нефти (с.у), доли ед.
        :param dens_gas: Плотность сеперированного газа (с.у), доли ед.
        :param solubility: газосодержание, м3 / м3
        :return: Объемный коэфицент м3 / м3
        """

        dens_rel = solubility * (dens_gas / dens_oil) ** 0.5
        brackets = cls.FVF_k3 * dens_rel + cls.FVF_k4 * temp - cls.FVF_k5
        return cls.FVF_k1 + cls.FVF_k2 * brackets**cls.FVF_k6
