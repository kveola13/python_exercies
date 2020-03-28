def print_first_and_last(list):
    first_and_last = [list[0], list[len(list) - 1]]
    return first_and_last


def main():
    test_list = [5, 10, 15, 20, 25]
    print(print_first_and_last(test_list))


if __name__ == '__main__':
    main()
