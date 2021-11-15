def bubble_sort(arr):
    # the time complexity: best O(n), worst O(n*n)
    # use a boolean in inner loop to control whether swap or not
    no_swap = True
    tmp = 0
    for i in range(len(arr), 0, -1):
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                no_swap = False
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
        if no_swap:
            break
    return arr


print(bubble_sort([1, 3, 2]))
print(bubble_sort([4, 3, 1, 2]))
print(bubble_sort([1, 2, 4, 3, 8, 9, 7, 11, 33, 12]))