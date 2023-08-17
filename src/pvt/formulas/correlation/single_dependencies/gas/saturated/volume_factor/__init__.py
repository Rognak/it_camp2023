from .abstract import VolumeFactorCorrelation
from .lee import Lee
from typing import Dict, Type


Famous: Dict[str, Type[VolumeFactorCorrelation]] = {
    "lee": Lee,
}
