from typing import Union
from pvt.formulas.correlation.single_dependencies.oil.saturated.viscosity.abstract import (
    DeadOilViscosityCorrelation,
    LiveOilViscosityCorrelation,
)
from pvt.formulas.correlation.base import TempUnit, DensityUnit, SolubilityUnit
import math


class LiveBeggs(LiveOilViscosityCorrelation):
    @classmethod
    def calc(
        cls,
        deed_viscosity: Union[float, int],
        solubility: Union[float, int],
    ) -> Union[float, int]:
        """
        :param deed_viscosity: вязкость дгазированной нефти, доли ед.
        :param solubility: газосодержание, м3 / м3
        :return: вязкость нефти
        """
        solubility = SolubilityUnit.SI.convert_to_foot_per_barrel(solubility)
        degree = 5.44 * (solubility + 150) ** (-0.338)
        multiplier = 10.715 * (solubility + 100) ** (-0.515)
        return multiplier * deed_viscosity**degree


class DeadBeggs(DeadOilViscosityCorrelation):
    VIS_k1 = 3.0324
    VIS_k2 = 0.02023
    VIS_k3 = -1.163

    @classmethod
    def __dead_oil_correlation_less_70f(
        cls,
        temp: Union[float, int],
        dens_oil: Union[float, int],
    ) -> Union[float, int]:
        """
        :param temp: Температура, F
        :param dens_oil: Плотность дгазированной нефти, доли ед.
        :return: Вязкость
        """
        vis70 = cls.__dead_oil_correlation_more_70f(70, dens_oil)
        vis80 = cls.__dead_oil_correlation_more_70f(80, dens_oil)
        c = math.log10(vis70 / vis80) / math.log10(80 / 70)
        b = vis70 * 70**c
        return 10 ** (math.log10(b) - c * math.log10(temp))

    @classmethod
    def __dead_oil_correlation_more_70f(
        cls,
        temp: Union[float, int],
        dens_oil: Union[float, int],
    ) -> Union[float, int]:
        """
        :param temp: Температура, F
        :param dens_oil: Плотность дгазированной нефти, доли ед.
        :return: Вязкость
        """
        x = (10 ** (cls.VIS_k1 - cls.VIS_k2 * dens_oil)) * (temp**cls.VIS_k3)
        return (10**x) - 1

    @classmethod
    def calc(
        cls,
        temp: Union[float, int],
        dens_oil: Union[float, int],
    ) -> Union[float, int]:
        """
        :param temp: Температура, K
        :param dens_oil: Плотность дгазированной нефти, доли ед.
        :return: Вязкость
        """
        temp = TempUnit.Kelvin.convert_to_fahrenheit(temp)

        if temp > 205:
            print(f"Температура {temp}F/{temp}K выше возможной в рамках корреляции")
            temp = 205

        dens_oil = DensityUnit.Relative.convert_to_api(dens_oil)

        if temp < 70:
            return cls.__dead_oil_correlation_less_70f(temp, dens_oil)
        else:
            return cls.__dead_oil_correlation_more_70f(temp, dens_oil)
