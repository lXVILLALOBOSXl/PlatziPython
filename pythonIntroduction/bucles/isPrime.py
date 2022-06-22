def isPrime(number):
    count = 2
    while count < number:
        if number % count == 0:
            return False
        count += 1
    return True
        

def run():
    inputNumber = int(input("What is the number that you want to know if is prime or isn't? : "))
    if not isPrime(inputNumber) or inputNumber == 1 or inputNumber == 0:
        print(str(inputNumber) + " isn't Prime")
    else: 
        print(str(inputNumber) + " is Prime")


if __name__ == '__main__':
    run()
