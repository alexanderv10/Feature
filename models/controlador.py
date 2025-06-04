from models.estudiante import Estudiante
from models.carrera import Carrera
from models.objetivo import Objetivo
from models.registro_historial import RegistroHistorial

class Controlador:
    @staticmethod
    def crear_estudiante_con_historial():
        objetivos = [
            Objetivo(nombre="Desarrollar software"),
            Objetivo(nombre="Administrar bases de datos"),
            Objetivo(nombre="Implementar redes"),
        ]
        carrera = Carrera(nombre="Sistemas", objetivos=objetivos)
        historial = [
            RegistroHistorial(semestre=1, avance_objetivos={
                "Desarrollar software": 80,
                "Administrar bases de datos": 95,
                "Implementar redes": 90,
            }),
            RegistroHistorial(semestre=2, avance_objetivos={
                "Desarrollar software": 82,
                "Administrar bases de datos": 96,
                "Implementar redes": 90,
            }),
        ]
        estudiante = Estudiante(id_estudiante=1, nombre="Alexander Vera", carrera=carrera, historial=historial)
        return estudiante
