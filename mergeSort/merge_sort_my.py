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
    return


print(merging_arrays([1, 10, 50], [2, 14, 90, 100]))
