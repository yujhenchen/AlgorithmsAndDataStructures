from queues import Queue


def print_queue(queue):
    print(queue.data)
    print("length of queue: " + str(queue.length))
    print()


def test_push():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print_queue(queue)
    return queue


def test_pop():
    queue = test_push()
    print(queue.pop())
    print_queue(queue)

    print(queue.pop())
    print_queue(queue)
