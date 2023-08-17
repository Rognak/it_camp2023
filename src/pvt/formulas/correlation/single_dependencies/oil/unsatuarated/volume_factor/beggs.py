from typing import Union
import math
from pvt.formulas.correlation.single_dependencies.oil.unsatuarated.volume_factor.abstract import (
    VolumeFactorCorrelation,
)
from pvt.formulas.correlation.base import (
    DensityUnit,
    SolubilityUnit,
    TempUnit,
    PresUnit,
)


class Beggs(VolumeFactorCorrelation):
    c1 = -1.433 * 10**-5
    c2 = 5 * 10**-5
    c3 = 17.2 * 10**-5
    c4 = -1.180 * 10**-5
    c5 = 12.61 * 10**-5

    @classmethod
    def compressibility(
        cls,
        temp: Union[float, int],
        bubble_point_pressure: Union[float, int],
        solubility: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        temp = TempUnit.Kelvin.convert_to_fahrenheit(temp)
        dens_oil = DensityUnit.Relative.convert_to_api(dens_oil)
        solubility = SolubilityUnit.SI.convert_to_foot_per_barrel(solubility)

        numerator = (
            cls.c1
            + cls.c2 * solubility
            + cls.c3 * temp
            + cls.c4 * dens_gas
            + cls.c4 * dens_oil
        )
        if bubble_point_pressure != 0:
            return numerator / bubble_point_pressure
        else:
            return numerator

    @classmethod
    def calc(
        cls,
        pressure: Union[float, int],
        temperature: Union[float, int],
        bubble_point_pressure: Union[float, int],
        bubble_point_solubility: Union[float, int],
        bubble_point_fvf: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        bubble_point_pressure = PresUnit.Pa.convert_to_psi(bubble_point_pressure)
        pressure = PresUnit.Pa.convert_to_psi(pressure)
        compressibility = cls.compressibility(
            temperature,
            bubble_point_pressure,
            bubble_point_solubility,
            dens_oil,
            dens_gas,
        )
        delta_press = bubble_point_pressure - pressure
        value = bubble_point_fvf * math.exp(compressibility * delta_press)
        return value
