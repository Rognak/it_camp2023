from shapely.geometry import LineString


def _make_line_repr(source: dict):
    return LineString(
        [
            (round(source["q_liq"][i], 2), round(source["p_wf"][i], 2))
            for i in range(len(source["q_liq"]))
        ]
    )


def calc_nodal(vlp: dict, ipr: dict):
    """
    Расчёт точки пересечения VLP vs IPR

    Parameters
    ----------
    vlp : dict
        Словарь, содержащий VLP
    ipr : dict
        Словарь, содержащий IPR
    """
    # Можно использовать numpy или библиотеку Shapely, LineString intersection
    vlp_line = _make_line_repr(vlp)
    ipr_line = _make_line_repr(ipr)
    intersection = vlp_line.intersection(ipr_line)
    return [{"q_liq": q, "p_wf": p} for q, p in intersection.coords]
