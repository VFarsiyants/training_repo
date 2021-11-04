def binary_search(search_list, item):
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = search_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    list_example = [1, 3, 5, 7, 9]
    search_3_index = binary_search(list_example, 3)
    search_7_index = binary_search(list_example, 7)
    print(search_3_index)
    print(search_7_index)

