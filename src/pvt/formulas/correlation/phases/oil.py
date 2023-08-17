from __future__ import annotations
from typing import Union, TYPE_CHECKING, Optional, Callable
from pvt.formulas.correlation.single_dependencies import oil as oil_cor
from pvt.formulas.correlation.phases.abstract import Phase, NormalVolume

if TYPE_CHECKING:
    from pvt.formulas.correlation.phases.gas import GasPhase

import numpy as np
import os


class OilPhase(Phase):
    def __init__(
        self,
        density_oil: Union[float, int],
        gas_model: Optional[GasPhase] = None,
        saturated_volume_factor_correlation: str = "beggs",
        unsaturated_volume_factor_correlation: str = "beggs",
        dead_viscosity_correlation: str = "beggs",
        saturated_viscosity_correlation: str = "beggs",
        unsaturated_viscosity_correlation: str = "noviscosibility",
        bubble_point_pressure_correlation: str = "beggs",
        limiting_solubility_correlation: str = "beggs",
    ) -> None:
        self.dens = density_oil
        self.sat = SaturatedModel(
            saturated_volume_factor_correlation,
            dead_viscosity_correlation,
            saturated_viscosity_correlation,
            limiting_solubility_correlation,
        )
        self.unsat = UnSaturatedModel(
            unsaturated_volume_factor_correlation,
            unsaturated_viscosity_correlation,
            bubble_point_pressure_correlation,
        )
        self.gas = gas_model

    def is_saturated(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> bool:
        gor = normal_condition_value.gor
        dens_gas = self.gas.dens if self.gas is not None else 1
        max_sol = self.sat.sol.calc(pres, temp, self.dens, dens_gas)
        return max_sol <= gor

    def calc_viscosity(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> Union[float, int]:
        if self.gas is None:
            return self.sat.calc_viscosity(0, temp, self.dens, 1)

        elif self.is_saturated(normal_condition_value, pres, temp):
            density_gas = self.gas.dens
            return self.sat.calc_viscosity(pres, temp, self.dens, density_gas)

        else:
            density_gas = self.gas.dens
            gor = normal_condition_value.gor
            bpp = self.unsat.bpp.calc(temp, gor, self.dens, self.gas.dens)
            bpp_visc = self.sat.calc_viscosity(bpp, temp, self.dens, density_gas)
            bpp_sol = self.sat.sol.calc(pres, temp, self.dens, density_gas)
            fun = self.unsat.calc_viscosity
            return fun(pres, temp, self.dens, density_gas, bpp_visc, bpp_sol)

    def calc_fvf(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> Union[float, int]:
        if self.gas is None:
            return 1

        elif self.is_saturated(normal_condition_value, pres, temp):
            density_gas = self.gas.dens
            return self.sat.calc_fvf(pres, temp, self.dens, density_gas)

        else:
            density_gas = self.gas.dens
            gor = normal_condition_value.gor
            bpp = self.unsat.bpp.calc(temp, gor, self.dens, self.gas.dens)
            bpp_fvf = self.sat.calc_fvf(bpp, temp, self.dens, density_gas)
            gor = normal_condition_value.gor
            fun = self.unsat.calc_fvf
            value = fun(pres, temp, self.dens, density_gas, bpp_fvf, gor)
            return value

    def calc_density(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> Union[float, int]:
        if self.gas is None:
            return self.dens * 1000

        elif self.is_saturated(normal_condition_value, pres, temp):
            density_gas = self.gas.dens
            return self.sat.calc_density(pres, temp, self.dens, density_gas)

        else:
            density_gas = self.gas.dens
            gor = normal_condition_value.gor
            bpp = self.unsat.bpp.calc(temp, gor, self.dens, self.gas.dens)
            bpp_fvf = self.sat.calc_fvf(bpp, temp, self.dens, density_gas)
            fun = self.unsat.calc_density
            return fun(pres, temp, self.dens, density_gas, bpp_fvf, gor)

    def calc_value(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
    ) -> Union[float, int]:
        vfv = self.calc_fvf(normal_condition_value, pres, temp)
        return normal_condition_value.oil * vfv


class SaturatedModel:
    def __init__(
        self,
        saturated_volume_factor_correlation: str = "beggs",
        dead_viscosity_correlation: str = "beggs",
        saturated_viscosity_correlation: str = "beggs",
        limiting_solubility_correlation: str = "beggs",
    ) -> None:
        self.fvf = oil_cor.sut.fvf.Famous[saturated_volume_factor_correlation]
        self.sol = oil_cor.sut.sol.Famous[limiting_solubility_correlation]

        self.dvisc = oil_cor.sut.vis.FamousDead[dead_viscosity_correlation]
        self.lvisc = oil_cor.sut.vis.FamousLive[saturated_viscosity_correlation]

    def calc_viscosity(
        self,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        dead_visc = self.dvisc.calc(temp, dens_oil)
        sol = self.sol.calc(pres, temp, dens_oil, dens_gas)
        return self.lvisc.calc(dead_visc, sol)

    def calc_fvf(
        self,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        sol = self.sol.calc(pres, temp, dens_oil, dens_gas)
        return self.fvf.calc(temp, dens_oil, dens_gas, sol)

    def calc_density(
        self,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        sol = self.sol.calc(pres, temp, dens_oil, dens_gas)
        fvf = self.fvf.calc(temp, dens_oil, dens_gas, sol)
        return (1000 * dens_oil + 1.2217 * sol * dens_gas) / fvf

    def calc_value(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        vfv = self.calc_fvf(pres, temp, dens_oil, dens_gas)
        return normal_condition_value.oil * vfv


class UnSaturatedModel:
    def __init__(
        self,
        unsaturated_volume_factor_correlation: str = "beggs",
        unsaturated_viscosity_correlation: str = "noviscosibility",
        bubble_point_pressure_correlation: str = "beggs",
    ) -> None:
        self.vfv = oil_cor.unsut.fvf.Famous[unsaturated_volume_factor_correlation]
        self.visc = oil_cor.unsut.vis.Famous[unsaturated_viscosity_correlation]
        self.bpp = oil_cor.unsut.bpp.Famous[bubble_point_pressure_correlation]

    def calc_viscosity(
        self,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
        bpp_visc: Union[float, int],
        sol: Union[float, int],
    ) -> Union[float, int]:
        bpp = self.bpp.calc(temp, sol, dens_oil, dens_gas)
        return self.visc.calc(pres, bpp, bpp_visc)

    def calc_fvf(
        self,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
        bpp_fvf: Union[float, int],
        sol: Union[float, int],
    ) -> Union[float, int]:
        bpp = self.bpp.calc(temp, sol, dens_oil, dens_gas)
        return self.vfv.calc(pres, temp, bpp, sol, bpp_fvf, dens_oil, dens_gas)

    def calc_density(
        self,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
        bpp_fvf: Union[float, int],
        sol: Union[float, int],
    ) -> Union[float, int]:
        dens = 1000 * dens_oil + 1.2217 * sol * dens_gas
        fvf = self.calc_fvf(pres, temp, dens_oil, dens_gas, bpp_fvf, sol)
        dens1 = dens / fvf
        return dens1

    def calc_value(
        self,
        normal_condition_value: NormalVolume,
        pres: Union[float, int],
        temp: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
        bpp_fvf: Union[float, int],
        sol: Union[float, int],
    ) -> Union[float, int]:
        vfv = self.calc_fvf(pres, temp, dens_oil, dens_gas, bpp_fvf, sol)
        return normal_condition_value.oil * vfv
