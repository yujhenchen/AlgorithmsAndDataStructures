def search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1


print(search([1, 2, 6, 4, 7, 8, 9, 11, 13], 9))
