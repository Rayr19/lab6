limite_temperatura = 50

def ingresar_temperatura():
    return float(input("Ingrese temperatura: "))

def validar_temperatura(temp):
    if temp < 0:
        print("Error")
        return False
    return True

def evaluar_temperatura(temp):
    if temp > limite_temperatura:
        return "ALERTA"
    return "NORMAL"

def mostrar_resultado(estado):
    print("Estado:", estado)

temp = ingresar_temperatura()

if validar_temperatura(temp):
    estado = evaluar_temperatura(temp)
    mostrar_resultado(estado)