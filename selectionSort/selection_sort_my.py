def selection_sort(arr):
    # always let the first one to be min
    # swap if element smaller than the min
    # start from the next part of arr
    tmp_val = 0
    for start in range(len(arr)):
        for i in range(start, len(arr)):
            if arr[i] < arr[start]:
                tmp_val = arr[start]
                arr[start] = arr[i]
                arr[i] = tmp_val
    return arr


print(selection_sort([1, 3, 2]))
print(selection_sort([4, 3, 1, 2]))
print(selection_sort([1, 2, 4, 3, 8, 9, 7, 11, 33, 12]))
