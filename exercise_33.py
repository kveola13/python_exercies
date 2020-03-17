import json
from os import path

if path.exists('gwent.json'):
    with open('gwent.json', 'r') as file_reader:
        gwent = json.load(file_reader)
else:
    with open('gwent.json', 'w') as file_w:
        file_w.write("{\n\n}\n")
        gwent = json.load(file_w)


def add_character(file_name):
    name = input('Which character do you want to add?\n').title()
    race = input('What race is {}?\n'.format(name)).title()
    gwent[name] = race
    print(type(gwent))
    with open('gwent.json', 'w') as file_writer:
        json.dump(gwent, file_writer)
    print('{} is now in the file {}\n'.format(name, file_name))


def find_char():
    name = input("Name the character you want to know more about?\n").title()
    try:
        if gwent[name]:
            print('{} is a/an {}\n'.format(name, gwent[name]))
    except KeyError:
        print('{} is not in the file\n'.format(name))


def print_list():
    for char in gwent:
        print(char, ':', gwent[char])
    print()


def main():
    while True:
        choice = input('What do you want to do next? you can: add, find, see all or quit\n').capitalize()
        if choice == 'Quit':
            print('Good Bye')
            exit()
        elif choice == 'Add':
            add_character(gwent)
        elif choice == 'Find':
            find_char()
        elif choice == 'See all':
            print_list()


if __name__ == '__main__':
    main()
