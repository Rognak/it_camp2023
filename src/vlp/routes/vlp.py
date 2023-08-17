from fastapi import APIRouter
from vlp.schemas.base import VlpCalcResponse, VlpCalcRequest
from vlp.calculations.vlp import calc_vlp

router = APIRouter(prefix="/vlp", tags=["VLP"])


@router.post("/calculator")
async def calculate_vlp(vlp_in: VlpCalcRequest) -> VlpCalcResponse:
    data = vlp_in.dict()
    value = await calc_vlp(**data)
    return value
