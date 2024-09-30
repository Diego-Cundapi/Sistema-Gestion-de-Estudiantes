import time

def selector():
    return input('Seleccione una opcion \n'
                 'Presione 0 para finalizar el programa \n'
                 'Presione 1 para agregar un estudiante \n'
                 'Presione 2 para agregar una materia a un estudiante \n'
                 'Presione 3 para modificar la calificacion de una materia \n'
                 'Presione 4 para eliminar un alumno \n'
                 'Presione 5 para calcular el promedio de un estudiante \n'
                 'Presione 6 para listar todos los estudiantes con sus calificaciones\n')
    
def validateType(entrada, tipo, situacion):
    try:
        return tipo(entrada)
    except ValueError:
        return validateType(input(f"Se esperaba un dato de tipo {tipo.__name__}. Para {situacion} Inténtelo de nuevo: "), tipo, situacion)


def materias(dictMaterias, materia, calificacion, agregar_mas):
    dictMaterias.update({materia: calificacion})
    
    if agregar_mas == 'si':
        return materias(dictMaterias, input('Ingrese la siguiente materia: '), float(input('Ingrese la calificación de la materia: ')), input('¿Desea agregar más materias? (si/no): '))
    else:
        return dictMaterias

def addEstudent(dictEstudents, nombre):
    dictEstudents.update({nombre: materias({}, input('Ingrese la materia: '), validateType(input('Ingrese la calificación: '),float, 'la calificacion'), input('¿Desea agregar más materias? (si/no): '))})
    
    print('\n¡Alumno Agregado con Exito!\n')
    time.sleep(2)
    return menu(dictEstudents, selector())

def addMateria(dictEstudents, nombre):
    if not dictEstudents:
        print("No hay estudiantes registrados.")
    elif nombre not in dictEstudents:
        print(f'Estudiante \"{nombre}\" no encontrado')
    else:
        dictEstudents.update({nombre: materias(dictEstudents[nombre], input('Ingrese la materia: '), validateType(input('Ingrese la calificación: '),float, 'la calificacion'), input('¿Desea agregar más materias? (si/no): '))})
        print('\n¡Materias añadidas con exito!')

    print()
    time.sleep(2)
    return menu(dictEstudents, selector())

def modifyValue(dictMaterias, materia, calificacion):
    if(materia in dictMaterias):
        return {**dictMaterias, materia: calificacion}
    else:
        print('Materia no encontrada')
        return modifyValue(dictMaterias,input('Ingrese nuevamente el nombre de la materia: '), calificacion)
    
def updateScore(dictEstudents, nombre):
    if nombre not in dictEstudents:
        print(f'Estudiante \"{nombre}\" no encontrado')
    else:
        dictEstudents.update({nombre: modifyValue(dictEstudents[nombre], input('Ingrese la materia: '), validateType(input('Ingrese la calificación: '),float, 'la calificacion'))})
        print('\n¡Calificacion Actualizada con Exito!')
    
    print()
    time.sleep(2)
    return menu(dictEstudents, selector())
        
    
def delStudent(dictEstudents, nombre):
    if nombre not in dictEstudents:
        print(f'Estudiante \"{nombre}\" no encontrado\n')
    else:
        del dictEstudents[nombre]
        print(f'¡El alumno \"{nombre}\" fue eliminado con Exito!')
    
    print()
    time.sleep(2)
    return menu(dictEstudents, selector())

def average(dictEstudents, nombre):
    if not dictEstudents:
        print("No hay estudiantes registrados.\n")
    elif nombre not in dictEstudents:
        print(f'Estudiante \"{nombre}\" no encontrado\n')
        time.sleep(2)
        return menu(dictEstudents, selector())
    else:
        print(f'El promedio es: ' , round(sum(list(map(lambda value: value,dictEstudents[nombre].values()))) / len(list(map(lambda value: value,dictEstudents[nombre].values()))),2))
    
    print()
    time.sleep(2)
    return menu(dictEstudents, selector())

def listAllStudents(dictEstudents):
    if not dictEstudents:
        print("No hay estudiantes registrados.")
    else:
        # Usamos map para aplicar una función a cada estudiante y sus materias
        print()
        list(map(lambda estudiante: (
            print(f'Estudiante: {estudiante}'),
            list(map(lambda materia: print(f'   {materia}: {dictEstudents[estudiante][materia]}'),
                     dictEstudents[estudiante].keys()))
        ), dictEstudents.keys()))
        
    print()
    time.sleep(2)
    return menu(dictEstudents, selector())


def menu(dictEstudents, opcion):
    if opcion == '0':
        print('Fin del Programa')
    elif opcion == '1':
        addEstudent(dictEstudents, input('Nombre del alumno: '))
    elif opcion == '2':
        addMateria(dictEstudents, input('Nombre del alumno: '))
    elif opcion == '3':
        updateScore(dictEstudents, input('Nombre del alumno: '))
    elif opcion == '4':
        delStudent(dictEstudents, input('Nombre del alumno: '))
    elif opcion == '5':
        average(dictEstudents, input('Nombre del alumno: '))
    elif opcion == '6':
        listAllStudents(dictEstudents)
    else:
        print("Opción no válida. Intente nuevamente.")
        return menu(dictEstudents, selector())


# Ejecutamos el menú
menu(dict(), selector())
