
def same(array1, array2):
    # loop the first array to
    # find index of the square of each num in the second array
    # remove the element in the second array by the found index
    # return False if not found
    # return True outside the loop
    for num in array1:
        if pow(num, 2) in array2:
             del array2[array2.index(pow(num, 2))]
        else:
            return False
    return True

# Test
print(same([1, 2, 3], [4, 1, 9]))
print(same([1, 2, 3], [1, 9]))
print(same([1, 2, 3], [4, 1, 1]))