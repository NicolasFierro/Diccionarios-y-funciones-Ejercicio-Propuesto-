# Diccionario para almacenar la información de los equipos
equipos = {}

# Función para agregar un equipo de cómputo con su ID, cargador, mouse y ambiente
def agregarEquipo(idEquipo, cargador, mouse, ambiente):
    # Verificar si el equipo ya existe en el diccionario
    if idEquipo in equipos:
        print("El equipo con ID {} ya existe.".format(idEquipo))
    else:
        equipos[idEquipo] = {'cargador': cargador, 'mouse': mouse, 'ambiente': ambiente, 'novedades': []}
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
        print("Ambiente: {}".format(equipo['ambiente']))
        print("Novedades:")
        for novedad in equipo['novedades']:
            print("- Fecha: {}, Descripción: {}".format(novedad['fecha'], novedad['descripcion']))
    else:
        print("El equipo con ID {} no existe.")

# Función para eliminar un equipo
def eliminarEquipo(idEquipo):
    if idEquipo in equipos:
        del equipos[idEquipo]
        print("Equipo con ID {} eliminado exitosamente.".format(idEquipo))
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Función para eliminar el mouse de un equipo
def eliminarMouse(idEquipo):
    if idEquipo in equipos:
        equipos[idEquipo]['mouse'] = None
        print("Mouse del equipo con ID {} eliminado exitosamente.".format(idEquipo))
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Función para eliminar el cargador de un equipo
def eliminarCargador(idEquipo):
    if idEquipo in equipos:
        equipos[idEquipo]['cargador'] = None
        print("Cargador del equipo con ID {} eliminado exitosamente.".format(idEquipo))
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Función para modificar la información de un equipo
def modificarEquipo(idEquipo, cargador, mouse, ambiente):
    if idEquipo in equipos:
        if cargador:
            equipos[idEquipo]['cargador'] = cargador
        if mouse:
            equipos[idEquipo]['mouse'] = mouse
        if ambiente:
            equipos[idEquipo]['ambiente'] = ambiente
        print("Información del equipo con ID {} modificada exitosamente.".format(idEquipo))
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Función para mostrar todos los equipos en un ambiente específico
def equiposEnAmbiente(ambiente):
    print("Equipos en el ambiente '{}':".format(ambiente))
    for idEquipo, equipo in equipos.items():
        if equipo['ambiente'] == ambiente:
            print("- ID del equipo: {}".format(idEquipo))
            print("  Cargador: {}".format(equipo['cargador']))
            print("  Mouse: {}".format(equipo['mouse']))
            print("  Ambiente: {}".format(equipo['ambiente']))

# Función para mostrar un menú interactivo
def mostrarMenu():
    while True:
        print("\nMenú:")
        print("1. Agregar equipo")
        print("2. Agregar novedad")
        print("3. Buscar equipo")
        print("4. Eliminar equipo")
        print("5. Eliminar mouse")
        print("6. Eliminar cargador")
        print("7. Modificar equipo")
        print("8. Mostrar equipos en un ambiente")
        print("9. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4/5/6/7/8/9): ")

        if opcion == '1':
            idEquipo = input("Ingrese el ID del equipo: ")
            cargador = input("Ingrese el cargador: ")
            mouse = input("Ingrese el mouse: ")
            ambiente = input("Ingrese el ambiente: ")
            agregarEquipo(idEquipo, cargador, mouse, ambiente)
        elif opcion == '2':
            idEquipo = input("Ingrese el ID del equipo al que desea agregar una novedad: ")
            fecha = input("Ingrese la fecha de la novedad: ")
            descripcion = input("Ingrese la descripción de la novedad: ")
            agregarNovedad(idEquipo, fecha, descripcion)
        elif opcion == '3':
            idEquipo = input("Ingrese el ID del equipo que desea buscar: ")
            buscarEquipo(idEquipo)
        elif opcion == '4':
            idEquipo = input("Ingrese el ID del equipo que desea eliminar: ")
            eliminarEquipo(idEquipo)
        elif opcion == '5':
            idEquipo = input("Ingrese el ID del equipo al que desea eliminar el mouse: ")
            eliminarMouse(idEquipo)
        elif opcion == '6':
            idEquipo = input("Ingrese el ID del equipo al que desea eliminar el cargador: ")
            eliminarCargador(idEquipo)
        elif opcion == '7':
            idEquipo = input("Ingrese el ID del equipo que desea modificar: ")
            cargador = input("Ingrese el nuevo cargador (deje en blanco para no modificar): ")
            mouse = input("Ingrese el nuevo mouse (deje en blanco para no modificar): ")
            ambiente = input("Ingrese el nuevo ambiente (deje en blanco para no modificar): ")
            modificarEquipo(idEquipo, cargador, mouse, ambiente)
        elif opcion == '8':
            ambiente = input("Ingrese el ambiente del que desea ver los equipos: ")
            equiposEnAmbiente(ambiente)
        elif opcion == '9':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    mostrarMenu()
