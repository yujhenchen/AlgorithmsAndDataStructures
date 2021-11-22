class Node(object):
    def __init__(self, value):
        super().__init__()
        self.next = None
        self.value = value


class SingleLinkedList:
    def __init__(self, head):
        super().__init__()
        self.head = head

    def push(self):
        return

    def pop(self):
        return

    def shift(self):
        return

    def unshift(self):
        return

    def get(self):
        return

    def set(self):
        return

    def insert(self):
        return

    def remove(self):
        return

    def reverse(self):
        return


if __name__ == "__main__":
    # test linked list nodes usage
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    head = node1
    while head is not None:
        print(head.value)
        head = head.next
