# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array
# a[start:stop:step] # start through not past stop, by step

nombre = input("¿Cuál es tu nombre?: ")
cutName = nombre[0]
print(cutName)
cutName = nombre[0:3]
print(cutName)
cutName = nombre[:3]
print(cutName)
cutName = nombre[3:]
print(cutName)
cutName = nombre[1:7]
print(cutName)
cutName = nombre[1:7:2]
print(cutName)
cutName = nombre[::]
print(cutName)
cutName = nombre[1::3]
print(cutName)
cutName = nombre[::-1]
print(cutName)