def run():
    for count in range(101):
        if count % 2 != 0:
            continue
        print(count)


if __name__ == '__main__':
    run()