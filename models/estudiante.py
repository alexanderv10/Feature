from dataclasses import dataclass, field
from typing import List, Optional, Dict
from models.carrera import Carrera
from models.registro_historial import RegistroHistorial

@dataclass
class Estudiante:
    id_estudiante: Optional[int]
    nombre: Optional[str]
    carrera: Carrera
    historial: List[RegistroHistorial] = field(default_factory=list)

    def progreso_por_objetivo(self) -> Dict[str, float]:
        suma_progresos = {obj.nombre: 0.0 for obj in self.carrera.objetivos}
        conteo = {obj.nombre: 0 for obj in self.carrera.objetivos}

        for registro in self.historial:
            for obj_nombre, progreso in registro.avance_objetivos.items():
                if obj_nombre in suma_progresos:
                    suma_progresos[obj_nombre] += progreso
                    conteo[obj_nombre] += 1

        promedio_progresos = {}
        for obj_nombre in suma_progresos:
            if conteo[obj_nombre] > 0:
                promedio = suma_progresos[obj_nombre] / conteo[obj_nombre]
            else:
                promedio = 0.0
            promedio_progresos[obj_nombre] = round(promedio, 2)

        return promedio_progresos

    def media_progreso_general(self) -> float:
        progreso_objetivos = self.progreso_por_objetivo()
        if not progreso_objetivos:
            return 0.0
        media = sum(progreso_objetivos.values()) / len(progreso_objetivos)
        return round(media, 2)
