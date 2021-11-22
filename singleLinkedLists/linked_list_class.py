class Node(object):
    def __init__(self, value):
        super().__init__()
        self.next = None
        self.value = value


if __name__ == "__main__":
    # test linked list nodes usage
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    head = node1
    while head is not None:
        print(head.value)
        head = head.next
