import asyncio

from fastapi import APIRouter

from aggregate.models.models import WellModelCalcRequest, WellModelCalcResponse
from aggregate.routes.request_formers import (
    form_ipr_request,
    form_nodal_request,
    form_vlp_request,
)
from aggregate.service_requests import ipr, nodal, vlp

main_router = APIRouter(prefix="/well_model", tags=["WellModel"])


@main_router.post("/calc", response_model=WellModelCalcResponse)
async def my_profile(data: WellModelCalcRequest):
    ipr_req = form_ipr_request(data)
    vlp_req = form_vlp_request(data)
    ipr_response = await ipr.calc_ipr(ipr_req)
    vlp_response = await vlp.calc_vlp(vlp_req)

    # ipr_response, vlp_response = await asyncio.gather(
    #     ipr.calc_ipr(ipr_req), vlp.calc_vlp(vlp_req)
    # )
    ipr_json = ipr_response.json()
    vlp_json = vlp_response.json()
    nodal_req = form_nodal_request(vlp_json, ipr_json)
    nodal_response = await nodal.calc_nodal(nodal_req)
    nodal_json = nodal_response.json()
    return dict(vlp=vlp_json, ipr=ipr_json, nodal=nodal_json)
