from aggregate.models.models import (
    IprCalcRequest,
    NodalCalcRequest,
    VlpCalcRequest,
    WellModelCalcRequest,
)


def form_vlp_request(well_model_request: WellModelCalcRequest):
    return VlpCalcRequest(
        inclinometry=well_model_request.inclinometry,
        casing=well_model_request.casing,
        tubing=well_model_request.tubing,
        pvt=well_model_request.pvt,
        p_wh=well_model_request.p_wh,
        geo_grad=well_model_request.geo_grad,
        h_res=well_model_request.h_res,
    ).dict()


def form_ipr_request(well_model_request: WellModelCalcRequest):
    return IprCalcRequest(
        p_res=well_model_request.p_res,
        wct=well_model_request.pvt.wct,
        pb=well_model_request.pvt.pb,
        pi=well_model_request.pi,
    ).dict()


def form_nodal_request(vlp_result, ipr_result):
    return NodalCalcRequest(vlp=vlp_result, ipr=ipr_result).dict()
