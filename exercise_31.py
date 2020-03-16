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
    guess_count = 6
    for char in random_word:
        char_list.append(char)
    while len(char_list) > 0 and guess_count > 0:
        if len(guess_list) > 0:
            for el in guess_list:
                print(el + ' ', end="")
                sys.stdout.flush()
            print()
        print("Guesses left: " + str(guess_count))
        for char in random_word:
            if char in guess_list:
                print(char + ' ', end="")
                sys.stdout.flush()
            else:
                print('_ ', end="")
                sys.stdout.flush()
        print()
        guess_letter = input('Guess a letter: \n').upper()
        if guess_letter not in char_list or guess_letter in guess_list:
            guess_count -= 1
        while guess_letter in char_list and guess_letter not in guess_list:
            char_list.remove(guess_letter)
            guess_list.append(guess_letter)
    if len(char_list) == 0:
        print('Congratulations! it took you ' + str(6 - guess_count) + ' to solve this')
    else:
        print('Sorry, you couldn\'t do it in time')
        print('The word was: ' + random_word)
    play_again = input('Play again? Y/N\n')
    if play_again.upper() == 'Y' or play_again.upper() == 'YES':
        hang_man()
    if play_again.upper() == 'N' or play_again.upper() == 'NO':
        exit()


def main():
    hang_man()


if __name__ == '__main__':
    main()
