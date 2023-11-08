# Diccionario para almacenar la información de los equipos
equipos = {}

# Función para agregar un equipo de cómputo con su ID, cargador y mouse
def agregarEquipo(idEquipo, cargador, mouse):
    # Verificar si el equipo ya existe en el diccionario
    if idEquipo in equipos:
        print("El equipo con ID {} ya existe.".format(idEquipo))
    else:
        equipos[idEquipo] = {'cargador': cargador, 'mouse': mouse, 'novedades': []}
        print("Equipo con ID {} agregado exitosamente.".format(idEquipo))

# Función para agregar una novedad a un equipo
def agregarNovedad(idEquipo, fecha, descripcion):
    if idEquipo in equipos:
        equipos[idEquipo]['novedades'].append({'fecha': fecha, 'descripcion': descripcion})
        print("Novedad agregada al equipo con ID {}.".format(idEquipo))
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Función para buscar un equipo por su ID y mostrar su información
def buscarEquipo(idEquipo):
    if idEquipo in equipos:
        equipo = equipos[idEquipo]
        print("ID del equipo: {}".format(idEquipo))
        print("Cargador: {}".format(equipo['cargador']))
        print("Mouse: {}".format(equipo['mouse']))
        print("Novedades:")
        for novedad in equipo['novedades']:
            print("- Fecha: {}, Descripción: {}".format(novedad['fecha'], novedad['descripcion']))
    else:
        print("El equipo con ID {} no existe.")

# Función para mostrar un menú interactivo
def mostrarMenu():
    while True:
        print("\nMenú:")
        print("1. Agregar equipo")
        print("2. Agregar novedad")
        print("3. Buscar equipo")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4): ")

        if opcion == '1':
            idEquipo = input("Ingrese el ID del equipo: ")
            cargador = input("Ingrese el cargador: ")
            mouse = input("Ingrese el mouse: ")
            agregarEquipo(idEquipo, cargador, mouse)
        elif opcion == '2':
            idEquipo = input("Ingrese el ID del equipo al que desea agregar una novedad: ")
            fecha = input("Ingrese la fecha de la novedad: ")
            descripcion = input("Ingrese la descripción de la novedad: ")
            agregarNovedad(idEquipo, fecha, descripcion)
        elif opcion == '3':
            idEquipo = input("Ingrese el ID del equipo que desea buscar: ")
            buscarEquipo(idEquipo)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    mostrarMenu()