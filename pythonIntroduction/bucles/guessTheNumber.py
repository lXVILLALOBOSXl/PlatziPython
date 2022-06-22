import random

def guessTheNumber(numberToGuess, numberInput):
    if numberInput == numberToGuess:
        return True
    return False


def main():

    welcomeMessage = """ 
    Welcome!  👾
    You have 5 chances to guess the number that the computer generates between 1 and 5,
    you have to get 2 points 
    Are you ready to lose? 😏
    """
    print(welcomeMessage)
    
    lifes = 5
    points = 0

    while(True):
        numberToGuess = random.randint(1, 5)
        numberInput = input("What is the number that you are imagining 💭 ?: ")
        if guessTheNumber(numberToGuess, int(numberInput)):
            points += 1
            if points == 2:
                print("CONGRATULATIOOOOONS, YOU WIN!!!! 🥳")
                break
            print("You guess correctly 😎, you have: " + str(points) + " points and " + str(lifes) + " lifes")
            continue
        lifes -= 1
        if lifes == 0:
            print("Sorry, you lose :( ")
            break
        print("Oh no, the numer was: " + str(numberToGuess) + ", you guess incorrectly 😪, you have: " + str(points) + " points and " + str(lifes) + " lifes")


if __name__ == '__main__':
    main()