# function inside function which is resursion and help to do things


def collect_odd_values(arr):
    odd_values = []

    def helper(input):
        # print(input)
        if len(input) == 0:
            return
        if input[0] % 2 != 0:
            odd_values.append(input[0])
        input.pop(0)
        helper(input)

    helper(arr)
    return odd_values


print(collect_odd_values([1, 2, 3, 4, 5, 6, 7, 8, 9]))
