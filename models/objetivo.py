from dataclasses import dataclass
from typing import Optional

@dataclass
class Objetivo:
    nombre: str
    descripcion: Optional[str] = None
    peso: float = 1.0