from pvt import formulas
from typing import Union, Tuple


def calc_rates(
    wct: Union[float, int],
    rp: Union[float, int],
    q_fluid: Union[float, int],
) -> formulas.correlation.phases.NormalVolume:
    wat = q_fluid * wct / 100
    oil = q_fluid - wat
    gas = oil * rp
    return formulas.correlation.phases.NormalVolume(oil=oil, wat=wat, gas=gas)


def calc_pvt(
    pres: Union[float, int],
    temp: Union[float, int],
    gamma_gas: Union[float, int],
    gamma_oil: Union[float, int],
    gamma_wat: Union[float, int],
    wct: Union[float, int],
    rp: Union[float, int],
    q_liquid: Union[float, int],
) -> Tuple[Union[float, int], Union[float, int], Union[float, int]]:
    oil = formulas.correlation.phases.Oil(gamma_oil)
    gas = formulas.correlation.phases.Gas(gamma_gas)
    wat = formulas.correlation.phases.Wat(gamma_wat)

    oil.gas = gas
    gas.oil = oil

    liq = formulas.correlation.phases.Liq(wat, oil)
    mix = formulas.correlation.phases.Mix(liq, gas)
    rates = calc_rates(wct, rp, q_liquid)

    mix_dens = mix.calc_density(rates, pres, temp)
    mix_visc = mix.calc_viscosity(rates, pres, temp)
    mix_rate = mix.calc_value(rates, pres, temp)

    return mix_rate, mix_visc, mix_dens
