from fastapi import APIRouter
from pvt.schemas.pvt import PvtIn, PvtOut
from pvt.service import calc_pvt

router = APIRouter(prefix="/calculator")


@router.post("")
async def calculate(input_data: PvtIn) -> PvtOut:
    pvt = calc_pvt(
        input_data.p,
        input_data.t,
        input_data.gamma_gas,
        input_data.gamma_oil,
        input_data.gamma_wat,
        input_data.wct,
        input_data.rp,
        input_data.q_liquid,
    )

    out = {
        "QMix": pvt[0] / (3600*24),
        "MuMix": pvt[1],
        "RhoMix": pvt[2],
    }

    return PvtOut(**out)
