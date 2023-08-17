from pydantic import BaseModel, Field


class PvtIn(BaseModel):
    p: float = Field(
        description="Давление, Па",
        alias="P",
    )
    t: float = Field(
        description="Температура, К",
        alias="T",
    )
    gamma_gas: float = Field(
        description="Относительная плотность газа, д.ед",
        alias="GammaGas",
    )
    gamma_wat: float = Field(
        description="Относительная плотность воды, д.ед",
        alias="GammaWat",
    )
    gamma_oil: float = Field(
        description="",
        alias="GammaOil",
    )
    wct: float = Field(
        description="Обводненность, %",
        alias="Wct",
    )
    rp: float = Field(
        description="Газовый фактор м3/м3",
        alias="Rp",
    )
    q_liquid: float = Field(
        description="Дебит жидкости, м3/сут",
        alias="QLiq",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "P": 10 * 10 ** 5,
                "T": 90 + 273,
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
    q_mix: float = Field(
        description="Расход смеси м3/с",
        alias="QMix",
    )
    mu_mix: float = Field(
        description="Вязкость смеси cP",
        alias="MuMix",
    )
    rho_mix: float = Field(
        description="Плотность смеси кг/м3",
        alias="RhoMix",
    )
