def collect_odd_values(arr):
    # use an array variable to collect element
    # if the length of the arr is 0, return empty array
    # if the first element is odd, append it to array variable
    # cat array variable with recursive fun to get all the odd element each recursion
    odd_arr = []

    if len(arr) == 0:
        return []
    if arr[0] %2 != 0:
        odd_arr.append(arr[0])
    arr.pop(0)
    odd_arr += collect_odd_values(arr)
    return odd_arr
print(collect_odd_values([1, 2, 3, 4, 5, 6, 7, 8, 9]))