def sum_range(num):
    print(num)
    if num == 1:
        return 1
    return num + sum_range(num - 1)

print(sum_range(10))
