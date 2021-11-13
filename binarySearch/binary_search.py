import math


def binary_search(arr, val):
    # get the middle value of arr and compare with val
    # min = middle if val > than middle else max = middle
    min_i = 0
    max_i = len(arr) -1
    middle = math.floor(len(arr) / 2)

    if len(arr) == 0:
        return -1

    if val == arr[middle]:
        return middle

    if val > arr[middle]:
        min_i = middle
    else:
        max_i = middle
    for i in range(min_i, max_i+1):
        #print(arr[i])
        if val == arr[i]:
            return i
    return -1


print(binary_search([], 2))
print(binary_search([0], 2))
print(binary_search([1, 2, 3], 2))
print(binary_search([5, 8, 13], 5))
print(binary_search([1, 2, 3, 4, 5], 5))
