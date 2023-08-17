from .abstract import SolubilityCorrelation
from .beggs import Beggs
from typing import Dict, Type


Famous: Dict[str, Type[SolubilityCorrelation]] = {
    "beggs": Beggs,
}
