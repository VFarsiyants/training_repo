def find_smallest(list_to_find):
    smallest = list_to_find[0]
    smallest_index = 0
    for i in range(len(list_to_find)):
        if smallest > list_to_find[i]:
            smallest = list_to_find[i]
            smallest_index = i
    return smallest_index


def selection_sort(list_to_sort):
    sorted_list = []
    for i in range(len(list_to_sort)):
        smallest_index = find_smallest(list_to_sort)
        sorted_list.append(list_to_sort.pop(smallest_index))
    return sorted_list


if __name__ == '__main__':
    list_example = [5, 3, 6, 2, 10]
    sorted_example = selection_sort(list_example)
    print(sorted_example)
