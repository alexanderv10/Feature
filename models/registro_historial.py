from dataclasses import dataclass
from typing import Dict

@dataclass
class RegistroHistorial:
    semestre: int
    avance_objetivos: Dict[str, float]  # progreso en % por nombre de objetivo
