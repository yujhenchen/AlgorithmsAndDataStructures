def count_down(num):
    if num == 0:
        return 0
    else:
        print(num)
        num = num -1
        return count_down(num)

print(count_down(10))