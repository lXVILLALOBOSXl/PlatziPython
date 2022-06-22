# Los diccionarios en Python son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. Identifican a cada elemento por una clave (Key). Se escriben entre {}.

# Operaciones en diccionarios
# .keys():Retorna la clave de nuestro elemento.

# .values(): Retorna una lista de elementos (valores del diccionario).

# .items(): Devuelve lista de tuplas (primero la clave y luego el valor).

# .clear(): Elimina todos los items del diccionario.

# .pop(“n”): Elimina el elemento ingresado.

def run():

    myDictionary = {
        'Volkswagen': 3060,
        'Tesla': 14301,
        'Toyota': 2156
    }

    print("Diccionario: " + str(myDictionary))
    print("Accediedno a valor mediante key Tesla: " + str(myDictionary['Tesla']))

    print("Recorriendo las keys de mi diccionario: ")
    for brand in myDictionary.keys():
        print(brand)

    print("Recorriendo los valores de mi diccionario: ")
    for value in myDictionary.values():
        print(value)

    print("Recorriendo mi diccionario: ")
    for brand, value in myDictionary.items():
        print("The " + brand + "'s value is: " + str(value)) 

if __name__ == '__main__':
    run()