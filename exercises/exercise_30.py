import random


def find_random_word():
    with open('SOWPODS.txt', 'r') as file_reader:
        lines = list(file_reader)
    return random.choice(lines).strip()


def main():
    print(find_random_word())


if __name__ == '__main__':
    main()
