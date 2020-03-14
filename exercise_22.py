def read_from_file():
    read_file_name = input('Please select file to read from\n')
    try:
        with open(read_file_name + '.txt', 'r') as read_file:
            whole_file = read_file.read()
        category_list = []
        for line in whole_file.split('\n'):
            category = line.split('/')[2]
            if category not in category_list:
                category_list.append(category)
        for el in category_list:
            print(el)
    except FileNotFoundError:
        print("Could not find file")
    finally:
        print("Enter a correct file name next time.")


def main():
    print("Please use the file: http://www.practicepython.org/assets/Training_01.txt")
    read_from_file()


if __name__ == '__main__':
    main()
