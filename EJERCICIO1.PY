medicamentos = 60000
despacho = 8000

print("Bienvenido",)
edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C o D): ").upper()
descuento_medicamentos = 0 

if edad <=30:
    if tramo == "A" or tramo == "B":
        descuento_medicamentos = 0.18
    elif tramo == "C" or tramo == "D":
        descuento_medicamentos = 0.12

elif 31 <=60:
    if tramo == "A" or tramo == "B":
        descuento_medicamentos = 0.12
    elif tramo == "C" or tramo == "D":
        descuento_medicamentos = 0.08

descuento_aplicado = int(medicamentos * descuento_medicamentos)
valor_final_medicamentos = int(medicamentos - descuento_aplicado)

descuento_despacho = 0

if tramo == "A" or tramo == "B":
    descuento_despacho += 0.10
if edad >=55:
    descuento_despacho += 0.05

valor_final_despacho = int(despacho - (despacho * descuento_despacho))
total = int(valor_final_medicamentos + valor_final_despacho)
print("--- RESULTADOS ---")
print("Valor final medicamentos: ", valor_final_medicamentos)
print("Total a pagar: ", total)

