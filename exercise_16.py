import random


def password_generator(length_of_password):
    num_list = list(range(0, length_of_password))
    return random.sample(num_list, length_of_password)


def main():
    print(password_generator(12))


if __name__ == '__main__':
    main()
