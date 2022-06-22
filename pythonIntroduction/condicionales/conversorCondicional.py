menu = """
Bienvenido al conversor de monedas 💸

1 - Pesos mexicanos 🇲🇽
2 - Euros 🇪🇺
3 - Libra esterlina 🇬🇧

Eliga una opcion:  """

opcion = input(menu)

if opcion == '1':
    monedaAConvertir = input("¿Cuántos pesos Mexicanos 🇲🇽 tienes? : ")
    monedaAConvertir = float(monedaAConvertir)
    valorDolar = 20.24
    dolares = monedaAConvertir / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares 💸")
elif opcion == '2':
    monedaAConvertir = input("¿Cuántos Euros 🇪🇺 tienes? : ")
    monedaAConvertir = float(monedaAConvertir)
    valorDolar = 0.95
    dolares = monedaAConvertir / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares 💸")
elif opcion == '3':
    monedaAConvertir = input("¿Cuántas libras esterlinas 🇬🇧 tienes? : ")
    monedaAConvertir = float(monedaAConvertir)
    valorDolar = 0.82
    dolares = monedaAConvertir / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares 💸")
else:
    print("Ingrese una opcion correcta e intentelo de nuevo")
