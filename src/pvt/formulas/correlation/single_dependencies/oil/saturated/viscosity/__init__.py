from .abstract import DeadOilViscosityCorrelation, LiveOilViscosityCorrelation
from .beggs_robinson_1975 import DeadBeggs, LiveBeggs
from typing import Dict, Type


FamousLive: Dict[str, Type[LiveOilViscosityCorrelation]] = {
    "beggs": LiveBeggs,
}

FamousDead: Dict[str, Type[DeadOilViscosityCorrelation]] = {
    "beggs": DeadBeggs,
}
