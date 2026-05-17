from random import randint

# INGRESO DE DATOS
num1 = int(input("Ingrese limite inferior: "))
num2 = int(input("Ingrese limite superior: "))

# GENERAR NUMERO ALEATORIO
numero = randint(num1, num2)

# AJUSTAR SI ES IMPAR
if numero % 2 != 0:
    if numero + 1 <= num2:
        numero = numero + 1
    else: 
        numero = numero -1

# ------------------------
# PRIMER INTENTO
# ------------------------
intento1 = int(input("Intente adivinar: "))
if intento1 == numero:
    print("Felicitaciones, adivinó en el primer intento. ") 
else:
    if intento1 < numero:
        print("El numero es mayor. ")
    else: 
        print("El numero es menor.")

# ------------------------ 
# SEGUNDO INTENTO
# ------------------------
intento2 = int(input("Intente de nuevo: "))

if intento2 == numero:
    print("Felicitaciones, adivinó en su segundo intento. ")

else:
    if intento2 < numero:
        print("El numero es mayor.")
    else:
        print("El numero es menor. ")

# PISTA
diferencia1 = abs(numero - intento1)
diferencia2 = abs(numero - intento2) 

print("Te dare una pista: ")

if diferencia1 < diferencia2:
    print("El numero que buscas esta mas cerca de", 
          intento2, "que de", intento1)
    
#-------------------------
# TERCER INTENTO
# -------------------------
intento3 = int(input("Intente laultima vez: "))

if intento3 == numero:
    print("Felicitaciones, pudiste adivinar. ")
else:
    print("Perdiste.")
    print("El numero era:" , numero)
