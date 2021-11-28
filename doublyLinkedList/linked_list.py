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
        # if length == 0, head and tail set to None
        # else, keep tail as node, set tail.prev as tail, node.prev = None, tail.next = None
        node = None
        if self.length >= 1:
            node = self.tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                node.prev = None
                self.tail = self.tail.prev
                self.tail.next = None
            self.length -= 1
        return node

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
