import math


def binary_search(arr, target):
    # get the middle_index of the array
    # given min_index and max_index of the arry
    # if the target > element at middle_index, set min_index = middle_index
    # else set max_index = middle_index
    # loop the array until min_index == max_index
    target_index = -1
    min_index = 0
    max_index = len(arr) - 1
    middle_index = math.floor(len(arr) / 2)
    if target == arr[middle_index]:
        return middle_index
    elif target > arr[middle_index]:
        min_index = middle_index
    else:
        max_index = middle_index

    for i in range(min_index, max_index + 1):
        if target == arr[i]:
            target_index = i
            break
    return target_index


print(binary_search([1, 2, 3, 4, 5, 6], 4))
print(binary_search([1, 2, 3, 4, 5, 6], 6))
print(binary_search([1, 2, 3, 4, 5, 6], 11))
