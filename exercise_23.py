def read_from_file_to_lists(first_file_name, second_file_name):
    first_list = []
    second_list = []
    with open(first_file_name + '.txt', 'r') as file_reader:
        while file_reader.readline() != "":
            first_list.append(file_reader.readline().strip('\n').strip(" "))
    with open(second_file_name + '.txt', 'r') as file_reader:
        while file_reader.readline() != "":
            second_list.append(file_reader.readline().strip('\n').strip(" "))
    return first_list, second_list


def find_overlapping_numbers_in_lists():
    first_file_name = "text1"
    second_file_name = "text2"
    common_list = []
    for el in read_from_file_to_lists(first_file_name, second_file_name)[0]:
        if el in read_from_file_to_lists(first_file_name, second_file_name)[1]:
            common_list.append(el)
    return common_list


def main():
    print(find_overlapping_numbers_in_lists())


if __name__ == '__main__':
    main()
