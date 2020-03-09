import math


def is_prime():
    num = int(input("Please enter a number\n"))
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False

    for div in range(3, int(math.sqrt(num)) + 1, 2):
        if num % div == 0:
            return False
    return True


def main():
    print("After entering a number, the program will tell you if the number is a prime or not.\n")
    print(is_prime())


if __name__ == '__main__':
    main()
