def sum_zero(array1):
    # Loop element from left of array and from the right of array
    # If right < left, return None
    # else if element at index left + element at index right == 0, return array1[left] and  array1[right]
    # else return None
    left = 0
    right = len(array1) - 1
    sumNum = 0
    while right >= left:
        #print(array1[left])
        #print(array1[right])
        sumNum = array1[left] + array1[right]
        if sumNum == 0:
            if left == right:
                return [array1[left]]
            else:
                return [array1[left], array1[right]]
        elif sumNum>0:
            right = right - 1
        else:
            left = left + 1

    return None


print(sum_zero([-3, -2, -1, 0, 1, 2, 3]))
print(sum_zero([-2, 0, 1, 3]))
print(sum_zero([1, 2, 3]))
print(sum_zero([0]))
