def bubble_sort(arr):
    # loop the arr, swap if the left > right
    # loop till the all elements are sorted
    tmp = 0
    for i in range(len(arr), 0, -1):
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
    return arr


print(bubble_sort([1, 3, 2]))
print(bubble_sort([4, 3, 1, 2]))
print(bubble_sort([1, 2, 4, 3, 8, 9, 7, 11, 33, 12]))