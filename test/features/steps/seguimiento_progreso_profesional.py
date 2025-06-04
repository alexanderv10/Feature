from behave import *
from models.estudiante import Estudiante
from models.carrera import Carrera
from models.objetivo import Objetivo
from models.registro_historial import RegistroHistorial

@step("que el estudiante tiene registrado al menos un historial de perfil")
def step_impl(context):
    objetivos = [
        Objetivo(nombre="Desarrollar software"),
        Objetivo(nombre="Administrar bases de datos"),
        Objetivo(nombre="Implementar redes"),
    ]
    carrera = Carrera(nombre="Sistemas", objetivos=objetivos)
    historial = [
        RegistroHistorial(semestre=1, avance_objetivos={
            "Desarrollar software": 60,
            "Administrar bases de datos": 55,
            "Implementar redes": 50,
        }),
        RegistroHistorial(semestre=2, avance_objetivos={
            "Desarrollar software": 65,
            "Administrar bases de datos": 68,
            "Implementar redes": 58,
        }),
    ]
    context.estudiante = Estudiante(id_estudiante=1, nombre="Alexander Vera", carrera=carrera, historial=historial)
    print(f"Dado: Estudiante '{context.estudiante.nombre}' de la carrera de '{carrera.nombre}' cuenta con un historial de perfil")

@step("el umbral de aceptación minimo es de {umbral:d}")
def step_impl(context, umbral):
    context.umbral_minimo = umbral
    print(f"y el umbral mínimo configurado es {context.umbral_minimo}")

@step('la carrera de sistemas tiene los siguientes "{objetivos}"')
def step_impl(context, objetivos):
    nombres_objetivos = [nombre.strip() for nombre in objetivos.split(",")]
    carrera = context.estudiante.carrera

    for nombre in nombres_objetivos:
        if not any(obj.nombre == nombre for obj in carrera.objetivos):
            carrera.objetivos.append(Objetivo(nombre=nombre))

    context.objetivos_de_carrera = nombres_objetivos
    print(f" y los objetivos agregados a la carrera son: {nombres_objetivos}")

@step("consulta el progreso del historial")
def step_impl(context):
    context.progresos = context.estudiante.progreso_por_objetivo()
    context.media = context.estudiante.media_progreso_general()
    print(f"Cuando: Se consulta el progreso: {context.progresos}")

@step("mostrara un porcentaje de progreso por cada objetivo")
def step_impl(context):
    for objetivo in context.objetivos_de_carrera:
        progreso = context.progresos.get(objetivo, None)
        assert progreso is not None, f"No se encontró el progreso para '{objetivo}'"
        assert 0 <= progreso <= 100, f"Progreso fuera de rango para '{objetivo}': {progreso}"
        assert progreso >= context.umbral_minimo, f"Progreso para '{objetivo}' ({progreso}) es menor que el umbral ({context.umbral_minimo})"
        print(f"Entonces: Progreso para '{objetivo}' = {progreso} - OK")

@step("se mostrara la media de progreso de estudiantes")
def step_impl(context):
    assert isinstance(context.media, (int, float)), "La media debe ser numérica"
    assert 0 <= context.media <= 100, "La media debe estar entre 0 y 100"
    assert context.media >= context.umbral_minimo, f"Promedio insuficiente: {context.media}"
    print(f"Entonces: Media de progreso general = {context.media} (umbral mínimo = {context.umbral_minimo}) - OK")


