# Sistema de Gestión de Alumnos
Este proyecto implementa un sistema de gestión de estudiantes para una escuela, diseñado para almacenar y procesar información de varios estudiantes, incluyendo sus nombres, materias y calificaciones.
Características principales

## Estructura de datos: Utiliza un diccionario anidado donde:
* Las claves del diccionario principal son los nombres de los estudiantes.
* Cada estudiante tiene asociado otro diccionario que contiene:

  * Materias como claves
  * Calificaciones correspondientes como valores

## Operaciones implementadas:

* Añadir un nuevo estudiante con sus materias y calificaciones
* Añadir una nueva materia a un estudiante existente
* Actualizar la calificación de una materia para un estudiante
* Eliminar un estudiante del sistema
* Calcular el promedio de calificaciones de un estudiante
* Listar todos los estudiantes con sus materias y calificaciones

## Detalles de implementación

El sistema está desarrollado en Python, aprovechando la flexibilidad de los diccionarios para manejar datos dinámicos.
Se utilizan funciones para cada operación, permitiendo una estructura modular y fácil de mantener.
La interfaz es por consola, ofreciendo un menú interactivo para realizar las diferentes operaciones.
