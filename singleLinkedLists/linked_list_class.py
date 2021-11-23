class Node(object):
    def __init__(self, value):
        super().__init__()
        self.next = None
        self.value = value


class SingleLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = None
            self.length += 1
        return self

    def pop(self):
        # if length is 1, set head and tail to None
        # else loop head till length-1 get the node before tail
        # set next of the node to None
        # set tail to the node
        # length --
        if self.length <= 1:
            self.head = None
            self.tail = None
        else:
            node_before_tail = self.head
            while node_before_tail.next is not self.tail:
                node_before_tail = node_before_tail.next
            node_before_tail.next = None
            self.tail = node_before_tail
        if self.length > 0:
            self.length -= 1
        return self

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