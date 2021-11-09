import math

def binary_search(arr, target):
    # the arr is sorted
    # get the middle element of arr
    # return index of the element if target == element
    if target not in arr:
        return -1

    middle_index = math.floor(len(arr) / 2)

    if arr[middle_index] == target:
        return middle_index

    if target < arr[middle_index]:
        for left in range(middle_index + 1):
            #print(left)
            if arr[left] == target:
                return left
    else:
        for right in range(len(arr)-1, middle_index, -1):
            #print(right)
            if arr[right] == target:
                return right


print(binary_search([1, 2, 3, 4, 5, 6], 4))
print(binary_search([1, 2, 3, 4, 5, 6], 6))
print(binary_search([1, 2, 3, 4, 5, 6], 11))
