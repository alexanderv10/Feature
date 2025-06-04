from behave import *
from models.estudiante import Estudiante
from models.carrera import Carrera
from models.objetivo import Objetivo
from models.registro_historial import RegistroHistorial
from models.controlador import Controlador

@step("que el estudiante tiene registrado al menos un historial de perfil")
def step_impl(context):
    context.estudiante = Controlador.crear_estudiante_con_historial()
    assert context.estudiante is not None, "El estudiante no fue creado"
    assert len(context.estudiante.historial) > 0, "El historial del estudiante está vacío"

@step("el umbral de aceptación minimo es de {umbral:d}")
def step_impl(context, umbral):
    context.umbral_minimo = umbral
    assert isinstance(context.umbral_minimo, int), "El umbral mínimo no es un entero"

@step('la carrera de sistemas tiene los siguientes "{objetivos}"')
def step_impl(context, objetivos):
    nombres_objetivos = [nombre.strip() for nombre in objetivos.split(",")]
    carrera = context.estudiante.carrera

    for nombre in nombres_objetivos:
        if not any(obj.nombre == nombre for obj in carrera.objetivos):
            carrera.objetivos.append(Objetivo(nombre=nombre))

    context.objetivos_de_carrera = nombres_objetivos
    assert hasattr(context, "objetivos_de_carrera"), "No se asignaron los objetivos de carrera"
    assert len(context.objetivos_de_carrera) > 0, "No se proporcionaron objetivos de carrera"

@step("consulta el progreso del historial")
def step_impl(context):
    context.progresos = context.estudiante.progreso_por_objetivo()
    context.media = context.estudiante.media_progreso_general()
    assert isinstance(context.progresos, dict), "El progreso debe ser un diccionario"
    assert isinstance(context.media, float), "La media debe ser un float"

@step("mostrara un porcentaje de progreso por cada objetivo")
def step_impl(context):
    for objetivo in context.objetivos_de_carrera:
        progreso = context.progresos.get(objetivo, None)
        assert progreso is not None, f"No se encontró el progreso para '{objetivo}'"
        assert 0 <= progreso <= 100, f"Progreso fuera de rango para '{objetivo}': {progreso}"
        assert progreso >= context.umbral_minimo, f"Progreso para '{objetivo}' ({progreso}) es menor que el umbral ({context.umbral_minimo})"

@step("se mostrara la media de progreso de estudiantes")
def step_impl(context):
    assert isinstance(context.media, (int, float)), "La media debe ser numérica"
    assert 0 <= context.media <= 100, "La media debe estar entre 0 y 100"
    assert context.media >= context.umbral_minimo, f"Promedio insuficiente: {context.media}"
