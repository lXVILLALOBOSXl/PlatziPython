def run():
    inputText = input("Give me a string: ")
    for char in inputText:
        if char == 'o':
            break
        print(char)


if __name__ == '__main__':
    run()