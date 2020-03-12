import random


def generate_rand_num():
    rand_num = [random.randint(1, 9) for num in range(0, 4)]
    rand_num = str(rand_num)
    return rand_num


def cows_and_bulls(rand_nums):
    cows = 0
    bulls = 0
    print("rand nums: " + rand_nums)
    user_input = list(int(input_num) for input_num in
                      input("Guess the numbers! Type four numbers with spaces to guess\n").strip().split())
    while len(user_input) != 4:
        user_input = list(int(input_num) for input_num in
                          input("Oops! You have to enter 4 numbers\n").strip().split())
    list_copy = list(map(int, rand_nums.strip("[]").split(',')))
    for el in range(len(user_input)):
        if user_input[el] in list_copy:
            print(str(user_input[el]) + " is in the list")
            cows += 1
        else:
            print(str(user_input[el]) + " is not in the list")
            bulls += 1
    return "cows: " + str(cows), "bulls: " + str(bulls)


def main():
    print(cows_and_bulls(generate_rand_num()))


if __name__ == '__main__':
    main()
