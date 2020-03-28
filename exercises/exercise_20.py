def binary_tree(ordered_list, number_to_search):
    list_copy = ordered_list
    while True:
        mid = int(len(list_copy) / 2)
        if number_to_search == list_copy[mid]:
            return True, "Found at index: " + str(mid)
        elif number_to_search < list_copy[mid]:
            list_copy = list_copy[:mid]
        elif number_to_search > list_copy[mid]:
            list_copy = list_copy[mid:]
        if len(list_copy) == 1:
            if number_to_search == list_copy[0]:
                return True, "Found at index: 0"
            return False, "Could not find number in list"


def main():
    ordered_list = [1, 3, 5, 30, 31, 42, 43, 500]
    print(binary_tree(ordered_list, 31)[1])
    print(binary_tree(ordered_list, 1)[1])
    print(binary_tree(ordered_list, 3)[1])
    print(binary_tree(ordered_list, 43)[1])
    print(binary_tree(ordered_list, 500)[1])
    print(binary_tree(ordered_list, 32)[1])
    print(binary_tree(ordered_list, 2)[1])
    print(binary_tree(ordered_list, 4)[1])
    print(binary_tree(ordered_list, 6)[1])
    print(binary_tree(ordered_list, 44)[1])


if __name__ == '__main__':
    main()
