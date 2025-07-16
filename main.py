estudiantes = {}

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Registrar estudiante")
    print("2. Mostrar todos los estudiantes y sus cursos")
    print("3. Buscar estudiante por carne")
    print("0. SALIR")

    opcion = input("Seleccione una opción: ")
    if opcion == "0":
        print("Saliendo del programa...")
        break
    elif opcion == "1":
        cantidad = int(input("Cuantos estudiantes desea registrar?: "))

        for i in range(cantidad):
            carne = input(f"Ingrese el número de carne del estudiante{i+1}: ")

            if carne in estudiantes:
                print("El número de carne ya está registrado. Intente con otro.")
            else:
                nombre = input("Ingrese el nombre del estudiante: ")
                edad = 0
                codigoCurso = ""
                nTarea = 0
                nExamen = 0
                nProyecto = 0

                while True:
                    try:
                        edad = int(input("Ingrese la edad del estudiante: "))
                        break
                    except ValueError:
                        print("Edad inválida.")

                carrera = input("Ingrese la carrera del estudiante: ")

                cursos = {}
                cantidadCursos = 0

                while True:
                    try:
                        cantidadCursos = int(input("Ingrese la cantidad de cursos que desea registrar: "))
                        break
                    except ValueError:
                        print("Cantidad de cursos inválida.")

                for j in range(cantidadCursos):
                    codigoCurso = input(f"Ingrese el código del curso {j + 1}: ")
                    while True:
                        try:
                            nTarea = int(input("Nota de tareas: "))
                            nExamen = int(input("Nota de examen: "))
                            nProyecto = int(input("Nota de proyecto: "))

                            if 0 <= nTarea <= 100 and 0 <= nExamen <= 100 and 0 <= nProyecto <= 100:
                                break
                        except ValueError:
                            print("Alguna cantidad inválida.")

                    cursos[codigoCurso] = {
                        "nota_tarea": nTarea,
                        "nota_examen": nExamen,
                        "nota_proyecto": nProyecto
                    }

                estudiantes[carne] = {
                    "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera,
                    "cursos": cursos
                }

        print("Estudiantes registrados exitosamente.*")
    elif opcion == "2":
        print("\nEstudiantes y sus cursos**")

        for carne, info in estudiantes.items():
            print(f"Carne: {carne}, Nombre: {info['nombre']}, Edad: {info['edad']}, Carrera: {info['carrera']}")

            for curso, notas in info['cursos'].items():
                print(f"  Curso: {curso}, Tarea: {notas['nota_tarea']}, Examen: {notas['nota_examen']}, Proyecto: {notas['nota_proyecto']}")
                suma = notas['nota_tarea'] + notas['nota_examen'] + notas['nota_proyecto']
                promedio = suma / 3
                print(f"        Promedio: {round(promedio,2)}")
    elif opcion == "3":
        print("Buscar estudiante por carne**")
        carne_buscar = input("Ingrese el número de carne del estudiante a buscar: ")
        if carne_buscar in estudiantes:
            info = estudiantes[carne_buscar]
            print(f"Carne: {carne_buscar}, Nombre: {info['nombre']}, Edad: {info['edad']}, Carrera: {info['carrera']}")

            for curso, notas in info['cursos'].items():
                print(f"  Curso: {curso}, Tarea: {notas['nota_tarea']}, Examen: {notas['nota_examen']}, Proyecto: {notas['nota_proyecto']}")
                suma = notas['nota_tarea'] + notas['nota_examen'] + notas['nota_proyecto']
                promedio = suma / 3
                print(f"        Promedio: {round(promedio,2)}")
        else:
            print("Estudiante no encontrado.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")