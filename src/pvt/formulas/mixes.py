def calc_q_mix(q_oil, q_wat, q_gas):
    return sum((q_oil, q_wat, q_gas))


def calc_rho_mix(rho_liq, gf, rho_gas):
    return rho_liq * (1 - gf) + gf * rho_gas


def calc_mu_mix(mu_liq, gf, mu_gas):
    return mu_liq * (1 - gf) + mu_gas * gf
