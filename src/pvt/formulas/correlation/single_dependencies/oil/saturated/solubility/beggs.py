from typing import Union
from pvt.formulas.correlation.single_dependencies.oil.saturated.solubility.abstract import (
    SolubilityCorrelation,
)


class Beggs(SolubilityCorrelation):
    RS_k1 = 1.2254503
    RS_k2 = 0.001638
    RS_k3 = 1.76875
    RS_k4 = 1.9243101395421235 * 10**-6
    RS_k5 = 1.2048192771084338

    @classmethod
    def calc(
        cls,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        """
        :param temp: Температуры, К
        :param pres: Давления, Па
        :param dens_oil: Плотности дегазированной нефти (с.у), доли ед.
        :param dens_gas: Плотность сеперированного газа (с.у), доли ед.
        :return: Газосодержание м3 / м3
        """
        yg = cls.RS_k1 + cls.RS_k2 * temp - cls.RS_k3 / dens_oil
        return dens_gas * (cls.RS_k4 * pres / 10**yg) ** cls.RS_k5
