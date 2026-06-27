from random import randint

#Flag para asegurar que el primer numero sea menor
#Try para asegurar que no se usen letras
flag_numero = True
while flag_numero == True:
    try:
        num1 = int(input("Ingrese límite inferior: "))
        num2 = int(input("Ingrese límite superior: ")) 
        if num1 < num2:
            numero = randint(num1, num2)
            flag_numero = False
        else:
            print("El primer numero debe ser menor que el segundo")
    except:
        print("Debe ingresar un numero entero.")

#Convirtiendo en numero par
if numero % 2 != 0:
    numero += 1
    if numero > num2:
        numero -= 2

#While para acierto
while True:
    #Intento 1
    intento1 = int(input("Intente adivinar: "))
    if intento1 < num1 or intento1 > num2:
        print("El numero debe estar entre el límite inferior y superior")
    elif intento1 == numero:
        print("Felicitaciones, adivinó en el primer intento.")
        break
    elif intento1 < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    #Intento 2
    intento2 = int(input("Intente de nuevo: "))
    if intento2 < num1 or intento2 > num2:
        print("El numero debe estar entre el límite inferior y superior")
    elif intento2 == numero:
        print("Felicitaciones, adivinó en su segundo intento.")
        break
    elif intento2 < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    #Pista
    print("Te daré una pista:")
    distancia1 = abs(numero - intento1)
    distancia2 = abs(numero - intento2)
    if distancia1 < distancia2:
        print(f"El número que buscas está más cerca de {intento1} que de {intento2}")
    else:
        print(f"El número que buscas está más cerca de {intento2} que de {intento1}")

    #Intento 3
    intento3 = int(input("Intente la última vez: "))
    if intento3 == numero:
        print("Felicitaciones, pudiste adivinar.")
    else:
        print("Perdiste.")
        print(f"El número era: {numero}")
    break