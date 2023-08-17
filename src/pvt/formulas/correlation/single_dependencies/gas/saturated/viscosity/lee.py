from typing import Union
import math
from pvt.formulas.correlation.single_dependencies.gas.saturated.viscosity.abstract import (
    ViscosityCorrelation,
)


class Lee(ViscosityCorrelation):
    @classmethod
    def calc(
        cls,
        temp: Union[float, int],
        dens_gas_standard: Union[float, int],
        dens_gas: Union[float, int],
        volume_factor: Union[float, int],
    ) -> Union[float, int]:
        """
        :param temp: Температура, K
        :param dens_gas_standard: Плотность дгазированной газа, доли ед.
        :param dens_gas: Приведенная плотность газа в стандартных условиях, доли ед.
        :param volume_factor: газосодержание, м3 / м3
        :return:
        """
        exp_mult = 2.57 + 1914.5 / 1.8 / temp + 0.275 * dens_gas_standard
        degree = volume_factor * (dens_gas / 1000) ** 1.11 + 0.04 * exp_mult
        multiplier1 = 10**-4 * (7.77 + 0.183 * dens_gas_standard)
        multiplier2 = (1.8 * temp) ** 1.5
        denomenator = 122.4 + 373.6 * dens_gas_standard + 1.8 * temp
        multiplier = multiplier1 * multiplier2 / denomenator
        return multiplier * math.exp(exp_mult * degree)
