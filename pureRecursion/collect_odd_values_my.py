def collect_odd_values(arr):
    # This is a failed solution
    # return if the array is empty
    # if the first element in the array is odd, append it
    # print(arr[0])
    if len(arr) == 0:
        return
    if (arr[0] %2 != 0):
        # print(arr[0])
        odd_val = arr[0]
        arr.pop(0)
        return collect_odd_values(arr).append(odd_val)
    else:
        arr.pop(0)
        return collect_odd_values(arr)

print(collect_odd_values([1, 2, 3, 4, 5, 6, 7, 8, 9]))