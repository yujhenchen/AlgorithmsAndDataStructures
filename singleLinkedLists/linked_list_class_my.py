class Node(object):
    def __init__(self, value) -> None:
        super().__init__()
        self.next = None
        self.value = value

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node1.set_next(node2)
    head = node1
    while head is not None:
        print(head.get_value())
        head = head.get_next()
