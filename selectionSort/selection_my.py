def selection_sort(arr):
    # loop the array till are elements are sorted
    # keep the min and move forward
    min_val = arr[0]
    curr_val = 0
    #move_min = False
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < min_val:
                curr_val = min_val
                min_val = arr[j]
                arr[j] = curr_val
                #move_min = True
        #if move_min:
        #    arr[i] = min_val
    return arr


print(selection_sort([1, 3, 2]))
print(selection_sort([4, 3, 1, 2]))
print(selection_sort([1, 2, 4, 3, 8, 9, 7, 11, 33, 12]))