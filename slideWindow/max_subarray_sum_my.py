import sys

def max_subarray_sum(arr, n):
    # define a window with 0 as start index and len of window which is n
    # give max_sum = 0
    # loop the array with window until the index of the len of the window is the len of the array -1
    # if the current sum of the window > than the max_sum, max_sum = sum of the window
    if n > len(arr):
        return None

    window = []
    max_sum = - sys.maxsize
    max_sum_start = 0
    for i in range(0, len(arr) - n + 1, 1):
        window = arr[i : n + i]
        # print(i)
        # print(window)
        if sum(window) > max_sum:
            max_sum = sum(window)
            max_sum_start = i
    return arr[max_sum_start:n], max_sum


print(max_subarray_sum([1, 2, 5, 2, 8, 1, 5], 2))
print(max_subarray_sum([1, 2, 5, 2, 8, 1, 5], 4))
print(max_subarray_sum([4, 2, 1, 6], 1))
print(max_subarray_sum([4, 2, 1, 6, 2], 4))
print(max_subarray_sum([], 4))
