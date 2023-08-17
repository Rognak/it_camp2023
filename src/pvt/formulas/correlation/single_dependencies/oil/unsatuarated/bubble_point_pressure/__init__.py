from .abstract import BubblePointPressureCorrelation
from .beggs import Beggs
from typing import Dict, Type


Famous: Dict[str, Type[BubblePointPressureCorrelation]] = {
    "beggs": Beggs,
}
