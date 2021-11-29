from stack import Stack


def print_stack(stack):
    print(stack.data)
    print("length of stack: " + str(stack.length))
    print()


def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print_stack(stack)
    return stack


def test_pop():
    stack = test_push()
    print(stack.pop())
    print_stack(stack)

    print(stack.pop())
    print_stack(stack)
