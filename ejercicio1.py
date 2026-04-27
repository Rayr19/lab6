limite_temperatura = 50

def mostrar_estado(temp):
    if  temp > limite_temperatura:
        print("Alerta: temperatura alta")
    else:
        print("Estado normal")

temperatura = float(input("Ingrese temperatura: "))
mostrar_estado(temperatura)