print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")
stock = 120
prestamos_activos = 0
historial_prestamos = 0

while True:
    print("\n===MENÚ PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")      
    if opcion == "1":
        print(f"Libros disponibles: {stock}")
    elif opcion == "2":
       try:
        cantidad = int(input("Cantidad de libros a prestar: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
        elif cantidad > stock:
            print("No hay suficientes libros disponibles para prestar.")
        else:
            stock -= cantidad
            prestamos_activos += cantidad
            historial_prestamos += 1
            print("Préstamo realizado correctamente.")

       except ValueError:
        print("Debe ingresar un número válido.")
    
    elif opcion == "3":
        try:
             cantidad = int(input("Cantidad de libros a devolver: "))
             if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
             elif stock + cantidad > 120:
                print("No es posible superar la capacidad máxima de 120 libros.")
             else:
                stock += cantidad
                 
                if cantidad <= prestamos_activos:
                    prestamos_activos -= cantidad
                else:
                    prestamos_activos = 0

                print("Devolución realizada correctamente.")

        except ValueError:
            print("Debe ingresar un número válido.")

    elif opcion == "4":
        print(f"Préstamos activos: {prestamos_activos}")
        print(f"Total de préstamos realizados durante la sesión: {historial_prestamos}")

    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    else:
        print("Opción no válida.")             
