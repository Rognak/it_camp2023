import math as mt


def calc_bg(p, t, z):
    gas_fvf = t * z * 350.958 / p
    return gas_fvf


def calc_gas_density(gamma_gas, bg):
    m = 28.97 * gamma_gas
    return m / (24.04220577350111 * bg)


def gas_viscosity_lee(t: float, gamma_gas: float, rho_gas: float) -> float:
    """
    Метод расчета вязкости газа по корреляции Lee
    Parameters
    ----------
    :param t: температура, К
    :param gamma_gas: относительная плотность газа, доли,
    (относительно в-ха с плотностью 1.2217 кг/м3 при с.у.)
    :param rho_gas: плотность газа при данном давлении температуре, кг/м3
    :return: вязкость газа, сПз
    -------
    """
    t_r = t * 1.8

    a = (7.77 + 0.183 * gamma_gas) * t_r ** 1.5 / (122.4 + 373.6 * gamma_gas +
                                                   t_r)
    b = 2.57 + 1914.5 / t_r + 0.275 * gamma_gas
    c = 1.11 + 0.04 * b
    gas_viscosity = 10 ** (-4) * a * mt.exp(b * (rho_gas / 1000) ** c)
    return gas_viscosity
