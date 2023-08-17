from .beggs import Beggs
from .abstract import VolumeFactorCorrelation
from typing import Dict, Type


Famous: Dict[str, Type[VolumeFactorCorrelation]] = {
    "beggs": Beggs,
}
