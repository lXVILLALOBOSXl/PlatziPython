# variable.strip(): El método strip eliminará todos los caracteres vacíos que pueda contener la variable

# variable.lower(): El método lower convertirá a las letras en minúsculas.

# variable.upper(): El método upper convertirá a las letras en mayúsculas.

# variable.capitalize(): El método capitalize convertirá a la primera letra de la cadena de caracteres en mayúscula.

# variable.replace (‘o’, ‘a’): El método replace remplazará un caracterer por otro. En este caso remplazará todas las ‘o’ por el caracter ‘a’.

# len(variable): Te indica la longitud de la cadena de texto dentro de la variable en ese momento.

nombre = input("¿Cuál es tu nombre?: ")
nombre = nombre.strip()
print(nombre)
nombre = nombre.lower()
print(nombre)
nombre = nombre.upper()
print(nombre)
nombre = nombre.capitalize()
print(nombre)
nombre = nombre.replace('o','a')
print(nombre)
cantidadDeCaracteres = len(nombre)
print("Numero de letras: " + str(cantidadDeCaracteres))

# Indices: variable[indice]

for i in range(len(nombre)):
    print(nombre[i])