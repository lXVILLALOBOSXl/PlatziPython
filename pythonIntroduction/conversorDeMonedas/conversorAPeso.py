dolares = input("¿Cuántos dólares tienes?: ")
dolares = float(dolares)
valorPeso = 0.049
pesos = dolares / valorPeso
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")