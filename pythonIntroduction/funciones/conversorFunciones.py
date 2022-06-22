def convertirADolar(moneda, valorEnDolar):
    monedaAConvertir = input("¿Cuántos pesos " + moneda + " tienes? : ")
    monedaAConvertir = float(monedaAConvertir)
    dolares = monedaAConvertir / valorEnDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares 💸")
    
menu = """
Bienvenido al conversor de monedas 💸

1 - Pesos mexicanos 🇲🇽
2 - Euros 🇪🇺
3 - Libra esterlina 🇬🇧

Eliga una opcion:  """

opcion = input(menu)

if opcion == '1':
    convertirADolar("Mexicanos 🇲🇽 ", 20.24)
elif opcion == '2':
    convertirADolar("Euros 🇪🇺", 0.95)
elif opcion == '3':
    convertirADolar("Libras Esterlinas 🇬🇧", 0.82)
else:
    print("Ingrese una opcion correcta e intentelo de nuevo")