def count_unique_values(array1):
    # if the next index is the length of the array, break
    # unique count +1 if the element at curr_index is different from element at next_index
    array_len = len(array1)

    if array_len == 0:
        return 0
    else:
        next_index = 0
        unique_count = 1
        for curr_index in range(len(array1)):
            next_index = curr_index+1
            if next_index == len(array1):
                break
            if array1[curr_index] != array1[next_index]:
                unique_count = unique_count + 1
        return unique_count


print(count_unique_values([1, 1, 1, 1, 1, 2]))
print(count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]))
print(count_unique_values([]))
print(count_unique_values([-2, -1, -1, 0, 1]))
