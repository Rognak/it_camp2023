from __future__ import annotations
from typing import Union, TYPE_CHECKING, Optional, Callable
from pvt.formulas.correlation.single_dependencies import gas as gas_cor
from pvt.formulas.correlation.phases.abstract import Phase, NormalVolume

if TYPE_CHECKING:
    from pvt.formulas.correlation.phases.oil import OilPhase

import numpy as np
import os


class GasPhase(Phase):
    def __init__(
        self,
        density_gas: Union[float, int],
        oil_model: Optional[OilPhase] = None,
        volume_factor_correlation: str = "lee",
        viscosity_correlation: str = "lee",
    ) -> None:
        self.dens = density_gas
        self.fvf = gas_cor.sat.fvf.Famous[volume_factor_correlation]
        self.vis = gas_cor.sat.visc.Famous[viscosity_correlation]
        self.oil = oil_model

    def calc_fvf(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> Union[float, int]:
        return self.fvf.calc(temp, pres, 1)

    def calc_viscosity(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> Union[float, int]:
        fvf = self.calc_fvf(normal_condition_value, pres, temp)
        cur_dens_gas = 28.97 * self.dens / 24.04220577350111 / fvf
        value = self.vis.calc(temp, self.dens, cur_dens_gas, fvf)
        if value is None:
            pass
        return value

    def calc_density(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> Union[float, int]:
        fvf = self.calc_fvf(normal_condition_value, pres, temp)
        return 28.97 * self.dens / 24.04220577350111 / fvf

    def calc_value(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> Union[float, int]:
        if self.oil is None:
            vfv = self.calc_fvf(normal_condition_value, pres, temp)
            return normal_condition_value.gas * vfv

        if not self.oil.is_saturated(normal_condition_value, pres, temp):
            return 0

        oil_dens = self.oil.dens
        max_sol = self.oil.sat.sol.calc(pres, temp, oil_dens, self.dens)
        delta_sol = normal_condition_value.gor - max_sol
        vfv = self.calc_fvf(normal_condition_value, pres, temp)
        return normal_condition_value.oil * delta_sol * vfv
