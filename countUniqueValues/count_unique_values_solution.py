def count_unique_values(arr):
    # return 0 of the length of array is 0
    # loop the array by the second element at index j
    # compare the previous element at index i
    arr_len = len(arr)
    if arr_len == 0:
        return 0

    pre_index = 0
    unique_arr = [arr[pre_index]]
    for j in range(1, arr_len):
        if arr[pre_index] != arr[j]:
            unique_arr.append(arr[j])
            pre_index = j
    print(unique_arr)
    return len(unique_arr)

print(count_unique_values([1, 1, 1, 1, 1, 2]))
print(count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]))
print(count_unique_values([]))
print(count_unique_values([-2, -1, -1, 0, 1]))