def sum_zero(array1):
    # Loop element in the array
    # Use 0 to minus the current element and get target element
    # if the target element in the array, return the element and the target element
    # else return None
    for i in range(len(array1)):
        target = 0 - array1[i]
        if target not in array1:
            return None
        if i == array1.index(target):
            return None
        return [array1[i], target]


print(sum_zero([-3, -2, -1, 0, 1, 2, 3]))
print(sum_zero([-2, 0, 1, 3]))
print(sum_zero([1, 2, 3]))
print(sum_zero([0]))