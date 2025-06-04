from dataclasses import dataclass
from typing import List
from models.objetivo import Objetivo

@dataclass
class Carrera:
    nombre: str
    objetivos: List[Objetivo]
