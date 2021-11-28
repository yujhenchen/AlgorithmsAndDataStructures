class Node(object):
    def __init__(self, value):
        super().__init__()
        self.next = None
        self.prev = None
        self.value = value


class DoublyLinkedList(object):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        # create new node
        # tail.next = node
        # node.prev = tail
        # tail = node
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return

    def pop(self):
        return

    def shift(self):
        return

    def unshift(self, value):
        return

    def get(self, index):
        return

    def set(self, index, value):
        return

    def insert(self, index, value):
        return

    def remove(self, index):
        return
