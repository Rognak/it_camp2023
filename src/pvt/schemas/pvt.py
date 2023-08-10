from pydantic import BaseModel, Field


class PvtIn(BaseModel):
    p: float = Field(description="Давление, Па", alias='P')
    t: float = Field(description="Температура, К", alias='T')
    gamma_gas: float = Field(description="Относительная плотность газа, д.ед", alias='GammaGas')
    gamma_wat: float = Field(description="Относительная плотность воды, д.ед", alias='GammaWat')
    gamma_oil: float = Field(description='', alias='GammaOil')
    wct: float = Field(description="Обводненность, %", alias='Wct')
    rp: float = Field(description="", alias='Rp')
    q_fluid: float = Field(description="Дебит жидкости", alias="QLiq")

    model_config = {
        "json_schema_extra": {
            "example":
                {
                    "P": 10,
                    "T": 90,
                    "GammaOil": 0.8,
                    "GammaGas": 0.7,
                    "GammaWat": 1,
                    "Wct": 50,
                    "Rp": 100,
                    "QLiq": 100,
                }
        }
    }


class PvtOut(BaseModel):
    q_mix: float = Field(description='', alias='QMix')
    mu_mix: float = Field(description='', alias='MuMix')
    rho_mix: float = Field(description='', alias='RhoMix')