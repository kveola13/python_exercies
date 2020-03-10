def fibbo_sequence(rotations):
    init_num = 1
    second_num = 1
    print(init_num)
    print(second_num)
    for num in range(rotations):
        sum_num = init_num + second_num
        init_num = second_num
        second_num = sum_num
        print(second_num)


def main():
    print(fibbo_sequence(6))


if __name__ == '__main__':
    main()
