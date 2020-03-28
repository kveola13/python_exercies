def write_to_file():
    file_to_save = input("Please enter file name\n")
    with open(file_to_save+'.txt', 'w') as open_file:
        open_file.write('Strings are coming')


def main():
    write_to_file()


if __name__ == '__main__':
    main()
