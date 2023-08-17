from .abstract import VolumeFactorCorrelation
from .beggs import Beggs
from typing import Dict, Type


Famous: Dict[str, Type[VolumeFactorCorrelation]] = {
    "beggs": Beggs,
}
