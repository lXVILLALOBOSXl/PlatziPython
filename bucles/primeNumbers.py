def isPrime(number):
    count = 2
    while count < number:
        if number % count == 0:
            return False
        count += 1
    return True
        

def run():
    inputNumber = int(input("Up to what number do you want to calculate the primes? : "))
    count = 0
    while count <= inputNumber:
        if not isPrime(count) or count == 1 or count == 0:
            print(str(count) + " isn't Prime")
        else: 
            print(str(count) + " is Prime")
        count+=1


if __name__ == '__main__':
    run()
