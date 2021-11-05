def sum_list(list_to_sum):
    if list_to_sum == []:
        return 0
    else:
        return list_to_sum[0] + sum_list(list_to_sum[1:])


def get_len(list_to_get_len):
    if list_to_get_len == []:
        return 0
    else:
        return 1 + get_len(list_to_get_len[1:])


def get_max(list_to_get_max):
    if get_len(list_to_get_max) == 2:
        return list_to_get_max[0] if list_to_get_max[0] >= list_to_get_max[1] else list_to_get_max[1]
    else:
        sub_max = get_max(list_to_get_max[1:])
        return list_to_get_max[0] if list_to_get_max[0] >= sub_max else sub_max


def quicksort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        pivot = list_to_sort[(len(list_to_sort) - 1) // 2]
        less = [i for i in list_to_sort if i < pivot]
        more = [i for i in list_to_sort if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)


if __name__ == "__main__":
    my_list = [5, 2, 4, 12, 6]
    print(sum_list(my_list))
    print(get_len(my_list))
    print(get_max(my_list))
    print(quicksort(my_list))
