import math


def gamma_oil_api(gamma_oil: float) -> float:
    return min((141.5 / gamma_oil - 131.5), 58)


def kelvin_to_fahr(T: float) -> float:
    return min(1.8 * (T - 273.15) + 32, 295)


def rs_m_to_rs_b(rs: float) -> float:
    return rs / 0.17810760667903522


def calc_gas_rate(bg, q_liq, wct, rp, rs):
    return bg * q_liq * (1 - wct) * (rp - rs)


def calc_wat_rate(q_liq, wct):
    return q_liq * wct


def calc_oil_rate(q_liq, wct, bo):
    return q_liq * (1 - wct) * bo


def calc_liq_rate(q_oil, q_wat):
    return q_oil + q_wat


def calc_wct(q_wat, q_liq):
    return q_wat / q_liq


def calc_gas_fraction(q_gas, q_mix):
    return q_gas / q_mix


def calc_v_mix(q_mix, d):
    return 4 * q_mix / (math.pi * d ** 2)


def calc_tvd(md, sina):
    return md * sina


def calc_rho_liq(rho_oil, wct, gamma_wat):
    return rho_oil * (1 - wct) + 1000 * wct * gamma_wat


def calc_mul(muo, muw, wc_rc):
    return muo * (1 - wc_rc) + muw * wc_rc
