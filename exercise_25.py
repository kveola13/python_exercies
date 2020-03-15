import random


def guessing_game():
    global mid
    guesses = 0
    robot_guess = 0
    test_target_number = random.randint(0, 100)
    number_list = []
    for el in range(0, 101):
        number_list.append(el)
    while not (len(number_list) == 1 or robot_guess == test_target_number):
        mid = round(len(number_list) / 2)
        robot_guess = number_list[mid]
        if robot_guess > test_target_number:
            number_list = number_list[:mid]
        if robot_guess < test_target_number:
            number_list = number_list[mid:]
        guesses += 1
    if robot_guess == test_target_number:
        return 'Found number ' + str(number_list[mid]) + ' after ' + str(guesses) + ' guesses'
    else:
        print('Robot\'s final guess: ' + str(number_list[mid]))


def main():
    print(guessing_game())


if __name__ == '__main__':
    main()
