import random


def common_list(list_a, list_b):
    temp_list = []
    list_copy = list_a
    for element in list_a:
        if element in list_b:
            temp_list.append(element)
            list_copy.remove(element)
    print("removed elements: " + list_copy.__str__())
    if len(temp_list) != 0:
        return temp_list
    else:
        return"no similar numbers"


def generate_list():
    return [random.randint(1, 10) for num in range(random.randrange(10, 15))]


def main():
    first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(common_list(first_list, second_list))
    print(generate_list())
    print(common_list(generate_list(), generate_list()))


if __name__ == '__main__':
    main()
