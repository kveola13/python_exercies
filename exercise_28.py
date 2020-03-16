def big_among_three(first, second, third):
    big_num = first
    if big_num < second:
        big_num = second
    if big_num < third:
        big_num = third
    return big_num


def main():
    print(big_among_three(3, 6, 5))


if __name__ == '__main__':
    main()
