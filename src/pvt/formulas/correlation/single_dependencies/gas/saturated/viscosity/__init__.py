from .abstract import ViscosityCorrelation
from .lee import Lee
from typing import Dict, Type


Famous: Dict[str, Type[ViscosityCorrelation]] = {
    "lee": Lee,
}
