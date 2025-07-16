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
    elif opcion not in ["1", "2", "3"]:
        print("Opción no válida. Por favor, intente de nuevo.")
        continue
    elif opcion == "1":
        print("*Nuevo estudiante*")
        carne = input("Ingrese el número de carne del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
    elif opcion == "2":

    elif opcion == "3":
