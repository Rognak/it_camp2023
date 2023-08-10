from pvt.formulas.mixes import calc_mu_mix, calc_rho_mix, calc_q_mix
from pvt.formulas.oil_params import calc_rs, calc_bo, calc_oil_density, oil_deadviscosity_beggs, oil_liveviscosity_beggs
from pvt.formulas.gas_params import calc_bg, calc_gas_density, gas_viscosity_lee
from pvt.formulas.base import calc_gas_rate, calc_oil_rate, calc_gas_fraction, calc_mul, calc_wct, calc_wat_rate, calc_liq_rate, calc_rho_liq

def calc_pvt(p, t, gamma_gas, gamma_oil, gamma_wat, wct, rp, q_fluid):
    q_fluid /= 86400
    rp *= gamma_oil

    rs = calc_rs(gamma_gas, gamma_oil, t, p)
    bo = calc_bo(rs, gamma_gas, gamma_oil, t)
    rho_oil = calc_oil_density(gamma_oil, rs, gamma_gas, bo)

    bg = calc_bg(p, t, 1)
    rho_gas = calc_gas_density(gamma_gas, bg)
    mu_dead = oil_deadviscosity_beggs(gamma_oil, t)

    # вязкости
    mu_oil = oil_liveviscosity_beggs(mu_dead, rs)
    mu_gas = gas_viscosity_lee(t, gamma_gas, rho_gas)

    # расходы
    q_gas = calc_gas_rate(bg, q_fluid, wct, rp, rs)
    q_oil_curr = calc_oil_rate(q_fluid, wct, bo)
    q_wat = calc_wat_rate(q_fluid, wct)

    q_mix = calc_q_mix(q_oil_curr, q_wat, q_gas)

    gas_fraction = calc_gas_fraction(q_gas, q_mix)

    q_l = calc_liq_rate(q_oil_curr, q_wat)
    new_wct = calc_wct(q_wat, q_l)
    mu_liq = calc_mul(mu_oil, 1, new_wct)

    mu_mix = calc_mu_mix(mu_liq, gas_fraction, mu_gas)

    rho_liq = calc_rho_liq(rho_oil, wct, gamma_wat)
    rho_mix = calc_rho_mix(rho_liq, gas_fraction, rho_gas)

    return q_mix, mu_mix, rho_mix

