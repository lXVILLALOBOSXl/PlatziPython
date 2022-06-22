import random

def defineElements(element):

    if element == 0:
        return ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
    elif element ==1:
        return ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    elif element == 2:
        return ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    else:
        return ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')

def run():
    password = ""

    while len(password) < 16:
        characters = defineElements(random.randint(0, 3))
        password += characters[random.randint(0, len(characters))]
    
    print("Your new password is: " + password)

if __name__ == '__main__':
    run()