pesos = input("¿Cuántos pesos Mexicanos tienes? ; ")
pesos = float(pesos)
valorDolar = 20.24
dolares = pesos / valorDolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")