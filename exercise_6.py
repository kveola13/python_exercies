def is_palindrome(string_list):
    # print(string_list[0::1])
    # print(string_list[::-1])
    return string_list[0::1] == string_list[::-1]


def main():
    print(is_palindrome("hello"))
    print(is_palindrome("heh"))


if __name__ == '__main__':
    main()
