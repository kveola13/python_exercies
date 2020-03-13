import math


def binary_tree(ordered_list, number_to_search):
    ordered_list.sort()
    list_copy = ordered_list
    low = list_copy[0]
    high = list_copy[len(list_copy) - 1]
    mid = round((len(list_copy)) / 2)
    if len(list_copy) == 1:
        return "Could not find number in list"
    else:
        while low <= high:
            print(len(list_copy))
            print(mid)
            if list_copy[mid] == number_to_search:
                return "Found at index: " + str(mid)
            elif len(list_copy) == 1:
                return "Could not find number in list"
            elif number_to_search < list_copy[mid]:
                list_copy = list_copy[:mid:]
                print(list_copy)
                binary_tree(list_copy, number_to_search)
            elif number_to_search > list_copy[mid]:
                list_copy = list_copy[mid::]
                print(list_copy)
                binary_tree(list_copy, number_to_search)


def main():
    ordered_list = [1, 3, 5, 30, 42, 43, 500]
    print(binary_tree(ordered_list, 45))
    # print(binary_tree(ordered_list, 9))


if __name__ == '__main__':
    main()
