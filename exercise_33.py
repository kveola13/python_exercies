def find_user_in_dict(dictionary):
    search = input("Please enter what you want to find..\n")
    if search in dictionary:
        return dictionary[search]
    return "That name could not be found.\n"


def main():
    test_dict = {
        "Geralt": "Witcher"
    }
    print(find_user_in_dict(test_dict))


if __name__ == '__main__':
    main()
