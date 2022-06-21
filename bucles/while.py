def run():
    numeroDePotencias = int(input("To what power do you want to raise the 2?: "))
    contador = 0
    while numeroDePotencias >= contador:
        print("2 raised to " + str(contador) + " is: " + str(2 ** contador))
        contador += 1

if __name__ == '__main__':
    run()