import random
import string


def password_generator(length_of_password):
    return ''.join(
        [random.choice(string.ascii_letters + string.digits + string.punctuation) for s in range(length_of_password)])


def main():
    print(password_generator(12))


if __name__ == '__main__':
    main()
