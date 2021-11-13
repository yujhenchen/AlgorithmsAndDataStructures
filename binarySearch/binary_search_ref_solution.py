import math


def binary_search(arr, val):
    # loop to set min and max by compare val and middle
    min_i = 0
    max_i = len(arr) - 1
    middle = math.floor(len(arr) / 2)
    find_i = -1
    if len(arr) == 0:
        return -1
    while True:
        if val == arr[middle]:
            find_i = middle
            break
        if val == arr[max_i]:
            find_i = max_i
            break
        if val == arr[min_i]:
            find_i = min_i
            break
        if val < arr[min_i] or val > arr[max_i]:
            break

        if val > arr[middle]:
            min_i = middle
        else:
            max_i = middle
        middle = math.floor((max_i + min_i) / 2)
    return find_i


print(binary_search([], 2))
print(binary_search([0], 2))
print(binary_search([1, 2, 3], 2))
print(binary_search([5, 8, 13], 5))
print(binary_search([1, 2, 3, 4, 5], 5))
