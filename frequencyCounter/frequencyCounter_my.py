def same(array1, array2):
    if len(array1) != len(array2):
        return False

    # keep the frequency of unique number in the array1 and array2
    # put the number and its frequency into a set1 and set2
    # loop the set1 and use the square of key to get value in set2
    # return False if get fail
    # return False if number does not match
    set1 = {}
    set2 = {}

    for i in range(len(array1)):
        if array1[i] in set1:
            set1[array1[i]] = set1[array1[i]] + 1
        else:
            set1[array1[i]] = 1
        if array2[i] in set2:
            set2[array2[i]] = set2[array2[i]] + 1
        else:
            set2[array2[i]] = 1

    for num in set1:
        if pow(set1[num], 2) not in set2:
            return False
        if set1[num] != set2[pow(set1[num], 2)]:
            return False
    return True


# Test
print(same([1, 2, 3], [4, 1, 9]))
print(same([1, 2, 3], [1, 9]))
print(same([1, 2, 3], [4, 1, 1]))