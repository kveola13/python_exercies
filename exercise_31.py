import sys

from exercise_30 import find_random_word


def remove_values_from_list(value_list, val):
    return [value for value in value_list if value == val]


def hang_man():
    random_word = find_random_word()
    # print(random_word)
    print("Hang Man")
    char_list = []
    guess_list = []
    guess_count = 0
    for char in random_word:
        char_list.append(char)
    while len(char_list) > 0:
        for char in random_word:
            if char in guess_list:
                print(char + ' ', end="")
                sys.stdout.flush()
            else:
                print('_ ', end="")
                sys.stdout.flush()
        print()
        guess_letter = input('Guess a letter: \n').upper()
        while guess_letter in char_list and guess_letter not in guess_list:
            char_list.remove(guess_letter)
            guess_list.append(guess_letter)
        guess_count += 1
        print(guess_list)
        print("Guess count " + str(guess_count))
    print('Congratulations! it took you ' + str(guess_count) + ' to solve this')


def main():
    hang_man()


if __name__ == '__main__':
    main()
