# Created by alex at 27/05/2025
# language: es

Característica: : Seguimiento de autoevaluación de progreso profesionalizante
  Como estudiante de la EPN
  Quiero conocer mi progreso a lo largo de cada semestre en relación a los objetivos de carrera
  Para determinar posibles falencias en mi proceso académico y tomar acciones correctivas

  #:)
 """ Escenario: Seguimiento sin falencias
    Dado que el estudiante tiene registrado al menos un historial de perfil
    Y el umbral de aceptación minimo es de 70
    Y la carrera de sistemas tiene los siguientes objetivos
      | Objetivo 1           | Objetivo 2                 | Objetivo 3        |
      | Desarrollar software | Administrar bases de datos | Implementar redes |
    Cuando consulta el progreso del historial
    Entonces mostrara un porcentaje de progreso por cada objetivo
    #feature_seguimiento_001
    Y se mostrara la media de progreso de estudiantes """

  Esquema del escenario: Seguimiento sin falencias
    Dado que el estudiante tiene registrado al menos un historial de perfil
    Y el umbral de aceptación minimo es de 70
    Y la carrera de sistemas tiene los siguientes "<objetivos>"
    Cuando consulta el progreso del historial
    Entonces mostrara un porcentaje de progreso por cada objetivo
    Y se mostrara la media de progreso de estudiantes
    Ejemplos:
    | objetivos                   |
    | Desarrollar software        |
    | Administrar bases de datos  |
    | Implementar redes           |


  #:(
  """Escenario: Seguimiento con falencias
    Dado que el estudiante tiene registrado al menos un historial de perfil
    Y umbral de aceptación minimo es de 70
    Cuando consulta el progreso del historial
    Entonces mostrara un porcentaje de progreso por cada objetivo
    Y se mostrara la media de progreso de estudiantes
    Y se mostrara una serie de recomendaciones"""
