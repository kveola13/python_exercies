def biggest(num_list):
    big_num = num_list[0]
    for num in num_list:
        if num > big_num:
            big_num = num
    return big_num


def main():
    num_list = [-5, -3, -2, 0, 1]
    print(biggest(num_list))


if __name__ == '__main__':
    main()
