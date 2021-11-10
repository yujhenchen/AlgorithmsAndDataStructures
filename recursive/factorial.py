# not recursive solution
# def factorial(num):
#     total = 1
#     for i in range(num,1,-1):
#         total *= i
#     return total

# Recursive solution
def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


print(factorial(4))
