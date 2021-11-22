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
    # use recursion
    # break array into 2 part with the middle element
    # when only element in each array, call merging_arrays to merge them back
    mid_i = math.floor(len(arr) / 2)
    arr1 = arr[:mid_i]
    arr2 = arr[mid_i :]
    #if len(arr1) == 1 and len(arr2) == 1:
    #    merging_arrays(arr1, arr2)

    print(arr1)
    print(arr2)
    print("---")
    if len(arr1) > 1:
        merge_sort(arr1)
    if len(arr2) > 1:
        merge_sort(arr2)


# test merging_arrays funciton
# print(merging_arrays([1, 10, 50], [2, 14, 90, 100]))

# test print recursive data
merge_sort([111, 10, 50, 2, 14, 90, 100])

#print(merge_sort([1, 10, 50, 2, 14, 90, 100]))
#print(merge_sort([111, 10, 50, 2, 14, 90, 100]))

