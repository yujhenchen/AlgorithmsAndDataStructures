
def valid_anagram(str1, str2):
    # Loop element in array1
    # if any of element in array1 not in array2, return flase
    # else move the first found element in array2
    # return true

    for char in str1:
        if len(str1) != len(str2):
            return False

        index = str2.find(char)
        if index == -1:
            return False
        else:
            str2 = str2[:index] + str2[index+1:]
            # print(index)
            # print(str2)
    return True


print(valid_anagram('',''))
print(valid_anagram('aaz','zza'))
print(valid_anagram('anagram','nagaram'))