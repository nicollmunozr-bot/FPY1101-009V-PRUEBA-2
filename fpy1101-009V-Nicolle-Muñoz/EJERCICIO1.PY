print("Hospital_Central_Metropolitano")
especialistas = 0
residentes = 0

while True:
    try:
        cantidad = int(input("¿Cuántos médicos desea registrar? "))
        if cantidad > 0:
            break
        else:
            print("¡Registro médico inválido! Ingrese un entero positivo para continuar.")
    except ValueError:
        print("¡Registro médico inválido! Ingrese un entero positivo para continuar.")

for i in range(cantidad):
    print(f"Registro del médico {i + 1}")
    while True:
        nombre = input("Ingrese nombre profesional: ")
        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("¡Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
    while True:
        try:
            experiencia = int(input("Ingrese años de experiencia: "))
            if experiencia > 0:
                break
            else:
                print("¡Error Clínico! Ingrese un entero positivo para continuar.")
        except ValueError:  
            print("¡Error Clínico! Ingrese un entero positivo para continuar.")
    if experiencia > 5:
        print("Clasificación: Especialista Senior")
        especialistas += 1
    else:
        print("Clasificación: Residente Junior")
        residentes += 1
print(f"Total de especialistas senior: {especialistas}")
print(f"Total de residentes junior: {residentes}")
print(f"¡El hospital cuenta con {especialistas} Especialistas Senior y {residentes} Residentes Junior!")
print("¡Registro médico completado con éxito!" , "¡Sistema listo para operar!")
