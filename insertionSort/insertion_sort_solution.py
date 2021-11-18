def insertion_sort(arr):
    # loop the arr forward to get the current element
    # loop the elements before current element backward
    # if the backward element is > current element,
    # copy previous backward into the next (for insert the  current element somewhere later)
    curr_val = 0
    for i in range(1, len(arr)):
        curr_val = arr[i]
        j = 0
        for j in range(i - 1, -1, -1):
            #print(j)
            if arr[j] > curr_val:
                arr[j + 1] = arr[j]
                #print(arr)
            else:
                break
        #print(j)
        arr[j + 1] = curr_val
    return arr


print(insertion_sort([1, 3, 2]))
print(insertion_sort([4, 3, 1, 2]))
print(insertion_sort([3, 4, 2, 1]))
print(insertion_sort([2, 1, 9, 7, 6, 4]))
print(insertion_sort([1, 2, 4, 3, 8, 9, 7, 11, 33, 12]))
