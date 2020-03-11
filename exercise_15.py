def return_reverse_words(long_string):
    split_string_with_space = long_string.split(" ")
    split_string_with_space = split_string_with_space[len(split_string_with_space) - 1::-1]
    return ' '.join(split_string_with_space)


def main():
    string_test = "this is a test"
    print(return_reverse_words(string_test))


if __name__ == '__main__':
    main()
