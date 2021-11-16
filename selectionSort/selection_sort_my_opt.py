def selection_sort(arr):
    # loop the sub arr per run
    # find min in sub arr
    # swap if current value < min
    tmp_val = 0
    min_val = 0
    min_i = 0
    for start in range(len(arr)):
        min_val = min(arr[start:])
        if arr[start] > min_val:
            min_i = arr.index(min_val)
            tmp_val = arr[start]
            arr[start] = arr[min_i]
            arr[min_i] = tmp_val
    return arr


print(selection_sort([1, 3, 2]))
print(selection_sort([4, 3, 1, 2]))
print(selection_sort([1, 2, 4, 3, 8, 9, 7, 11, 33, 12]))
