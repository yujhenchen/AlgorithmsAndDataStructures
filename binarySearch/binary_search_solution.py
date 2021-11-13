import math


def binary_search(arr, val):
    # move the min and max index forward to actually skip the none equal value
    min_i = 0
    max_i = len(arr) - 1
    middle = math.floor(len(arr) / 2)

    if len(arr) == 0:
        return -1

    while val != arr[middle]:
        if min_i > max_i:
            return -1
        if val > arr[middle]:
            min_i = middle + 1
        else:
            max_i = middle - 1
        middle = math.floor((min_i + max_i) / 2)
    return middle


print(binary_search([], 2))
print(binary_search([0], 2))
print(binary_search([1, 2, 3], 2))
print(binary_search([5, 8, 13], 5))
print(binary_search([1, 2, 3, 4, 5], 5))
