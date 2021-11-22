import math


def merging_arrays(arr1, arr2):
    # merged the 2 arrays and create another array that is also sorted
    # walk through elements in both array and comoare
    # push the smaller one into arr
    # push the rest elemtn in another array if one array arrives to the end
    arr = []
    curr_1 = 0
    curr_2 = 0
    while curr_1 < len(arr1) and curr_2 < len(arr2):
        arr.append(min(arr1[curr_1], arr2[curr_2]))
        arr.append(max(arr1[curr_1], arr2[curr_2]))
        curr_1 += 1
        curr_2 += 1

    if len(arr1) > len(arr2):
        arr.extend(arr1[curr_1:])
    else:
        arr.extend(arr2[curr_2:])
    return arr


def merge_sort(arr):
    # return the array if the length of the array is smaller or equal to 1
    # recursive slice the array into left and right
    # merge left and right from the bottom (when merge_sort return single element array at len(arr) <= 1)
    print(len(arr))
    if len(arr) <= 1:
        return arr

    mid_i = math.floor(len(arr) / 2)
    left = merge_sort(arr[:mid_i])
    right = merge_sort(arr[mid_i:])
    print(left)
    print(right)
    print()
    # merging_arrays(left, right)


# print(merge_sort([1, 10, 50, 2, 14, 90, 100]))
# print(merge_sort([111, 10, 50, 2, 14, 90, 100]))

merge_sort([111, 10, 50, 2, 14, 90, 100])

