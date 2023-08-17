from typing import Union
from pvt.formulas.correlation.phases.abstract import Phase, NormalVolume


class WatPhase(Phase):
    def __init__(
        self,
        density_wat: Union[float, int],
    ) -> None:
        self.dens = density_wat

    @classmethod
    def calc_viscosity(
        cls,
        normal_condition_value: NormalVolume,
        pressure: Union[float, int],
        temperature: Union[float, int],
    ) -> Union[float, int]:
        return 1

    @classmethod
    def calc_density(
        cls,
        normal_condition_value: NormalVolume,
        pressure: Union[float, int],
        temperature: Union[float, int],
    ) -> Union[float, int]:
        return 1000

    @classmethod
    def calc_value(
        cls,
        normal_condition_value: NormalVolume,
        pressure: Union[float, int],
        temperature: Union[float, int],
    ) -> Union[float, int]:
        return normal_condition_value.wat
