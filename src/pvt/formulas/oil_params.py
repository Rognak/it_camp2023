from pvt.formulas.base import gamma_oil_api as calc_api, kelvin_to_fahr, rs_m_to_rs_b
import math as mt


def calc_bo(rs, gamma_gas, gamma_oil, t):
    return 0.972 + 0.000147 * ((5.614583333333334 * rs * (
            (gamma_gas / gamma_oil) ** 0.5) + 2.25 * t - 574.5875) ** 1.175)


def calc_rs(gamma_gas, gamma_oil, t, p):
    yg = 1.2254503 + 0.001638 * t - 1.76875 / gamma_oil
    rs = gamma_gas * (1.9243101395421235e-06 * p / 10 ** yg) ** 1.2048192771084338
    return rs


def calc_oil_density(gamma_oil, rs, gamma_gas, bo):
    return 1000 * (gamma_oil + rs * gamma_gas * 1.2217 / 1000) / bo


def oil_deadviscosity_beggs(gamma_oil, t):
    """
    Метод расчета вязкости дегазированной нефти по корреляции Beggs
    Parameters
    ----------
    :param gamma_oil: относительная плотность нефти, доли,
    (относительно воды с плотностью 1000 кг/м3 при с.у.)
    :param t: температура, К
    :return: вязкость дегазированной нефти, сПз
    -------
    """
    # Ограничение плотности нефти = 58 API для корреляции Beggs and Robinson
    gamma_oil_api = calc_api(gamma_oil)

    # Ограничение температуры = 295 F для корреляции Beggs and Robinson
    t = kelvin_to_fahr(t)

    if t < 70:
        # Корректировка вязкости дегазированной нефти для температуры ниже 70 F
        # Расчет вязкости дегазированной нефти для 70 F
        oil_deadviscosity_beggs_70 = (10 ** (
                (10 ** (3.0324 - 0.02023 * gamma_oil_api)) * (70 ** (-1.163)))) - 1
        # Расчет вязкости дегазированной нефти для 80 F
        oil_deadviscosity_beggs_80 = (10 ** (
                (10 ** (3.0324 - 0.02023 * gamma_oil_api)) * (80 ** (-1.163)))) - 1
        # Экстраполяция вязкости дегазированной нефти по двум точкам
        c = mt.log10(oil_deadviscosity_beggs_70 /
                     oil_deadviscosity_beggs_80) / mt.log10(80 / 70)
        b = oil_deadviscosity_beggs_70 * 70 ** c
        oil_deadviscosity_beggs = 10 ** (mt.log10(b) - c * mt.log10(t))
    else:
        x = (10 ** (3.0324 - 0.02023 * gamma_oil_api)) * (t ** (-1.163))
        oil_deadviscosity_beggs = (10 ** x) - 1
    return oil_deadviscosity_beggs


def oil_liveviscosity_beggs(oil_deadvisc, rs):
    """
    Метод расчета вязкости нефти, насыщенной газом, по корреляции Beggs
    Parameters
    ----------
    :param oil_deadvisc: вязкость дегазированной нефти, сПз
    :param rs: газосодержание, (м3/м3)
    :return: вязкость, насыщенной газом нефти, сПз
    -------
    """
    # Конвертация газосодержания в куб. футы/баррель
    rs_new = rs_m_to_rs_b(rs)

    a = 10.715 * (rs_new + 100) ** (-0.515)
    b = 5.44 * (rs_new + 150) ** (-0.338)
    oil_liveviscosity_beggs = a * oil_deadvisc ** b
    return oil_liveviscosity_beggs
