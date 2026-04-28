limite_temp = 50
alertas_detectadas = 0

def validar_temperatura(t):
    return t >= 0

for i in range(1, 4):
    print(f"--- Sensor {i} ---")
    temp = float(input(f"Ingrese temperatura {i}: "))
    
    if validar_temperatura(temp):
        if temp > limite_temp:
            print("Estado: ALERTA")
            alertas_detectadas += 1
        else:
            print("Estado: NORMAL")
    else:
        print("Lectura inválida (No se puede procesar)")

print("\n================================")
print(f"Total de sensores en ALERTA: {alertas_detectadas}")
print("================================")