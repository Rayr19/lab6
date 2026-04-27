limite_temperatura = 50

def validar_temperatura(temp):
    if temp < 0:
        print("Error: temperatura invalida")
        return False
    return True

def mostrar_estado(temp):
    if  temp > limite_temperatura:
        print("Alerta")
    else:
        print("Normal")

temperatura = float(input("Ingrese temperatura: "))

if validar_temperatura(temperatura):
    mostrar_estado(temperatura)