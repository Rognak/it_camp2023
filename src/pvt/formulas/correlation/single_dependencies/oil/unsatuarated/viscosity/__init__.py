from .abstract import ViscosityCorrelation
from .no_viscosibility import NoViscosibility
from typing import Dict, Type


Famous: Dict[str, Type[ViscosityCorrelation]] = {
    "noviscosibility": NoViscosibility,
}
