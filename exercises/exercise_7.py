def print_even_numbers_from_list(number_list):
    even_num = [x for x in number_list if x % 2 == 0]
    print(even_num)


def main():
    number_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print_even_numbers_from_list(number_list)


if __name__ == '__main__':
    main()
