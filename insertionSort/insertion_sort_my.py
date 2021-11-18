def insertion_sort(arr):
    # loop the array current element curr_element
    # loop the pre array
    # compare each element in pre array
    # set curr_element to be next elemnt of element in pre array if curr_element > element in pre array
    sorted_ls = [arr[0]]
    for i in range(1, len(arr)):
        curr_i = len(sorted_ls) - 1
        while curr_i >= 0:
            if sorted_ls[curr_i] < arr[i]:
                sorted_ls.insert(curr_i+1 , arr[i])
                break
            else:
                if curr_i == 0:
                    sorted_ls.insert(0, arr[i])
                    break
            curr_i -= 1
    return sorted_ls


print(insertion_sort([1, 3, 2]))
print(insertion_sort([4, 3, 1, 2]))
print(insertion_sort([1, 2, 4, 3, 8, 9, 7, 11, 33, 12]))
