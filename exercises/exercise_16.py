import random
import string

from random_word import RandomWords


def password_generator(length_of_password):
    random_word = RandomWords()
    random_digit_list = []
    for num in range(length_of_password):
        random_digit_list.append(random.choice(string.digits))
    if length_of_password <= 4:
        return random_word.get_random_word() + random_word.get_random_word() + ''.join(random_digit_list)
    else:
        return ''.join(
            [random.choice(string.ascii_letters + string.digits + string.punctuation) for s in
             range(length_of_password)])


def main():
    print(password_generator(5))


if __name__ == '__main__':
    main()
