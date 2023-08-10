from fastapi import APIRouter

from ipr.models.models import IprCalcRequest, IprCalcResponse

main_router = APIRouter(prefix="/ipr", tags=["IPR"])


@main_router.post("/calc", response_model=IprCalcResponse)
async def calculate(ipr_in: IprCalcRequest):
    """Эндпоинт расчёта IPR"""
    from ipr.calculations.vogel_ipr import calc_ipr

    res = calc_ipr(p_res=ipr_in.p_res, pi=ipr_in.pi, wct=ipr_in.wct, pb=ipr_in.pb)
    return res
