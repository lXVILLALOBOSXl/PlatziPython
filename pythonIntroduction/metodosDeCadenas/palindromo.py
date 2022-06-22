def isPalindrome(inputWord):
    inputWord = inputWord.strip()
    inputWord = inputWord.lower()
    inputWord = inputWord.replace(" ", "")
    reverseWord = inputWord[::-1]
    if reverseWord == inputWord:
        return True
    else:
        return False


def run():
    inputWord = input("What is the word that you want to know if is palindrome or isn't? :")
    if isPalindrome(inputWord):
        print("Your word is palindrome")
    else:
        print("Your word isn't palindrome")

if __name__ == '__main__':
    run()

