import random


def guess_number():
    rand_num = random.randint(1, 9)
    guess_count = 0
    while 1:
        guess = input("Guess a number between 1 to 9\n")
        print(rand_num)
        if guess == "exit":
            print("Exiting...")
            break
        if int(guess) < rand_num:
            print("higher!")
            guess_count += 1
        if int(guess) > rand_num:
            print("lower!")
            guess_count += 1
        if int(guess) == rand_num:
            print("You guessed it! After " + str(guess_count) + " tries!")
            retry = input("Would you like to try again? Y/N\n")
            if retry.upper().lower() == "no" or retry.upper().lower() == "n":
                exit()


def main():
    guess_number()


if __name__ == '__main__':
    main()
