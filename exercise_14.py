def return_list_as_set(return_list):
    new_list = set(return_list)
    new_list = list(new_list)
    return new_list


def return_list(list_returning):
    new_list = []
    for el in list_returning:
        if el not in new_list:
            new_list.append(el)
    return new_list


def main():
    demo_list = [1, 2, 3, 12, 4, 1, 2, 4, 5, 6, 71, 1, 1, 14, 4, 5, 4, 7, 8]
    print(return_list_as_set(demo_list))
    print(return_list(demo_list))


if __name__ == '__main__':
    main()
