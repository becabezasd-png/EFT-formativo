#EFT formativo dia viernes

asignaturas = {
    'DSY1103': ['Fullstack', 'L4', 7, 42, 12],
    'FPY1101': ['Programacion', 'L6', 7, 21, 23],
    'OCY1101': ['CyberSeguridad', 'online', 4, 31, 14],
    'DSY1101': ['Cloud Computing', 'online', 4, 31, 6],
    'DSY1105': ['Aplicaciones Mobile','L9',5, 15, 21],
    'MDY3131': ['Base de Datos', 'L3', 5, 11, 12]
}

def iniciaFuncion(nombre):
    print(f"Inicia la funcion {nombre}")


def totalAlumnos(codigo):
    iniciaFuncion("Total Alumnos")

    asignatura = asignaturas[codigo]

    total = asignatura[3] + asignatura[4]
    print(total)
    return total

def totalAsignaturas():
    iniciaFuncion("Total asignaturas")

    cantidad_asignaturas = len(asignaturas)
    print(f"Total asignaturas: {cantidad_asignaturas}")
    return cantidad_asignaturas

def asignaturasPorSala(sala):
    iniciaFuncion("Asignaturas por sala")

    sala_asignaturas = []
    
    for datos in asignaturas.values():
        if datos[1] == sala:
            sala_asignaturas.append(datos[0])
    
    print(sala_asignaturas)
    return sala_asignaturas

def asignaturasOnline():
    iniciaFuncion("Asignaturas online")

    online = 'online'
    asignaturas_online = []

    for asignatura in asignaturas.values():
        if asignatura[1] == online:
            asignaturas_online.append(asignatura[0])
    print(f"Asignaturas online: {asignaturas_online}")

def asignaturasPorHoras(minimo, maximo):
    iniciaFuncion("Asignaturas por hora")
            
            



asignaturasOnline()