import math


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
                self.tail = self.tail.prev
                self.tail.next = None
            node.prev = None
            self.length -= 1
        return node

    def shift(self):
        # remove the first node
        node = None
        if self.length >= 1:
            node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        node.next = None
        self.length -= 1
        return node

    def unshift(self, value):
        # add a node to the beginning of the linked list
        node = Node(value)
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return

    def get(self, index):
        # return None if index >= length
        # check index is bigger or smaller than mid length
        # loop from head if index < mid length
        # loop from tail if index > mid length
        if index >= self.length:
            return None
        else:
            mid_length = math.floor(self.length / 2)
            node = None
            if index <= mid_length:
                node = self.head
                for i in range(index):
                    node = node.next
            else:
                node = self.tail
                for i in range(self.length, index + 1, -1):
                    node = node.prev
            return node

    def set(self, index, value):
        return

    def insert(self, index, value):
        return

    def remove(self, index):
        return

    def reverse(self):
        return
